#!/usr/bin/env python3

from aws_cdk import core

from pipeline.pipeline_inner_stack import PipelineInnerStack

app = core.App()
PipelineInnerStack(app,'PipelineInnerStack', env={
    'region': 'us-east-1'
})

app.synth()
