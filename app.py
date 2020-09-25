#!/usr/bin/env python3

from aws_cdk import core

from pipeline.pipeline_stack import PipelineStack
from pipeline.pipeline_inner_stack import PipelineInnerStack

app = core.App()
PipelineStack(app, "pipeline")
PipelineInnerStack(app,'PipelineInnerStack', env={
    'region': 'us-east-1'
})

app.synth()
