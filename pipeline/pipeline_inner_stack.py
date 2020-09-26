from os import path

from aws_cdk import core
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from aws_cdk import aws_codebuild as codebuild
from aws_cdk import pipelines

from .webservice_stage import WebServiceStage

class PipelineInnerStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope,id,**kwargs)

        this_dir = path.dirname(__file__)

        code_build_project = codebuild.PipelineProject(self, "demoServiceProject", 
            build_spec=codebuild.BuildSpec.from_source_filename('./java_services/DemoService/buildspec.yml'))

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()
        java_build_artifact = codepipeline.Artifact()

        pipeline = pipelines.CdkPipeline(self, 'Pipeline',
            cloud_assembly_artifact=cloud_assembly_artifact,
            pipeline_name='WebinarPipeline',
            source_action=cpactions.GitHubSourceAction(
                action_name='Github',
                output=source_artifact,
                oauth_token= core.SecretValue.secrets_manager('github-token'),
                owner='JuanGQCadavid',
                repo='cd_last_project_pipeline',
                trigger=cpactions.GitHubTrigger.POLL
            ),
            synth_action=pipelines.SimpleSynthAction(
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assembly_artifact,
                install_command='npm install -g aws-cdk && pip install -r requirements.txt',
                synth_command='cdk synth'
            )
        )

        build_action = cpactions.CodeBuildAction(
            input=source_artifact,
            outputs=[java_build_artifact],
            project=code_build_project,
            action_name="demoServicesBuildAction",
        )

        buildStage = pipeline.add_stage(stage_name="JavaBuild")
        buildStage.add_actions(build_action)

        pre_prod_stage = pipeline.add_application_stage(WebServiceStage(self,'Pre-prod', env={
            'region': 'us-east-1'
        }))

        pre_prod_stage.add_manual_approval_action(
            action_name='PromoteToProd')
        
        pipeline.add_application_stage(WebServiceStage(self,'Prod', env={
            'region': 'us-east-1'
        }))