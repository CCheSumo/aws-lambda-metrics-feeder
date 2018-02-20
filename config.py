from headers import Headers

class Config(object):
    url = ''
    headers = {
        Headers.content_type: 'application/vnd.sumologic.carbon2',
        Headers.content_encoding: 'deflate',
        Headers.x_sumo_source: 'metris_sla_aws_lambda_source',
        Headers.x_sumo_host: 'metrics_sla_aws_lambda_host',
        Headers.x_sumo_category: 'metrics_sla_lambda_category'
    }
    sleep_interval = 0.1
    request_interval = 0.1
    number_requests = 600
