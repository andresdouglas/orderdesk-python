from datetime import datetime


def test_connection(client):
    data = client.test_connection()

    assert data.get('status') == 'success', data.get('message')
    assert data.get('execution_time')
    assert data.get('message') == 'Connection Successful'
    assert data.get('current_date_time')

def test_create_order(client, order):
    res = client.create_order(order)
    assert 'success' == res.get('status')
    assert res.get('order')


def test_get_orders(client):
    data = client.get_orders(data=dict(
        search_start_date=datetime.isoformat(
            datetime(2014, 10, 8)),
        search_end_date=datetime.isoformat(
            datetime(2014, 10, 9)),
    ))

    assert data.get('status') == 'success'
    assert data.get('orders')
