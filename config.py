from header import Header

class Config(object):
    headers = {
        Header.content_type: 'application/vnd.sumologic.carbon2',
        Header.content_encoding: 'deflate',
        Header.x_sumo_source: 'metris_sla_aws_lambda_source',
        Header.x_sumo_host: 'metrics_sla_aws_lambda_host',
        Header.x_sumo_category: 'metrics_sla_lambda_category'
    }
    sleep_interval = 0.1
    request_interval = 1
    number_requests = 60
