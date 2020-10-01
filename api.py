import requests
import click

ORIG_HOST = 'ec2-13-210-116-179.ap-southeast-2.compute.amazonaws.com'
HOST = 'ec2-13-211-205-113.ap-southeast-2.compute.amazonaws.com'


headers = {"Key":"Content-Type","Value":"application/x-www-form-urlencoded","Description":""}

@click.command()
@click.option('--origin', is_flag=True)
@click.argument('filename', type=str)
def main(filename):
    if origin:
        host = ORIG_HOST
    else:
        host = HOST

    url = f'http://{host}:8000/gaddsDownload/'

    with open(filename) as fl:
        body = json.load(fl)
    r = requests.post(URL, headers=headers, json=body)
    print(r.status_code)
    print(r.content.decode('utf-8'))


if __name__ == '__main__':
    main()
