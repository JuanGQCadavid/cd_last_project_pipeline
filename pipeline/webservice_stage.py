from aws_cdk import core
from .pipeline_stack import PipelineStack

class WebServiceStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope,id,**kwargs)

        service = PipelineStack(self,"WebService")

        self.url_output = service.url_output