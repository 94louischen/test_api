import pika
from common.LogTools import DoLogs
from data.extract_data import ExtractData


def send_mq(interface_init):
    """
    RabbitMq发送消息
    :return:
    """
    try:
        credentials = pika.PlainCredentials(interface_init[0].get_value('mq_data', 'mq_username'),
                                            interface_init[0].get_value('mq_data', 'mq_pwd'))  # 登录mq
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(interface_init[0].get_value('mq_data', 'mq_host'), 5672, '/',
                                      credentials))  # 连接队列
        channel = connection.channel()  # 创建频道
        channel.queue_declare(queue=interface_init[0].get_value('mq_data', 'mq_name'), durable=True)  # 声明消息队列
        mq_content = interface_init[0].get_value('mq_data', 'mq_content')
        mq_content = mq_content.replace('5ae0df8a78e34c35bd0518fa95abb7b5', getattr(ExtractData, 'shareId'))
        channel.basic_publish(exchange='', routing_key='online_user_behavior_exchange_marking_tool',
                              body=bytes(str(mq_content), encoding="utf8"))  # 发送消息
        connection.close()
    except Exception:
        DoLogs(__name__).mylog.info("消息发生失败")
    finally:
        DoLogs(__name__).mylog.info("消息发送成功")


if __name__ == '__main__':
    send_mq()
