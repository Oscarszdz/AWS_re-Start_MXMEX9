{"changed":true,"filter":false,"title":"boto3_challenge.py","tooltip":"/boto3_challenge.py","value":"# Importing the required libraries\nimport boto3\nimport logging\nfrom botocore.exceptions import ClientError\nimport os\n\n\ndef create_bucket(bucket_name, region=None):\n    \"\"\"Create an S3 bucket in a specified region\n\n    If a region is not specified, the bucket is created in the S3 default\n    region (us-east-1).\n\n    :param bucket_name: Bucket to create\n    :param region: String region to create bucket in, e.g., 'us-west-2'\n    :return: True if bucket created, else False\n    \"\"\"\n\n    # Create bucket\n    try:\n        if region is None:\n            s3_client = boto3.client('s3')\n            s3_client.create_bucket(Bucket=bucket_name)\n        else:\n            s3_client = boto3.client('s3', region_name=region)\n            location = {'LocationConstraint': region}\n            s3_client.create_bucket(Bucket=bucket_name,\n                                    CreateBucketConfiguration=location)\n    except ClientError as e:\n        logging.error(e)\n        return False\n    return True\n\n\n# Retrieve the list of existing buckets\ns3 = boto3.client('s3')\nresponse = s3.list_buckets()\n\n# Output the bucket names\nprint('Existing buckets before creating:')\nfor bucket in response['Buckets']:\n    print(f'  {bucket[\"Name\"]}')\n    \n    \ncreate_bucket('boto3challenge', 'us-west-2')\n\n# Output the bucket names after bucket creation\ns3 = boto3.client('s3')\nresponse = s3.list_buckets()\nprint('Existing buckets after creating:')\nfor bucket in response['Buckets']:\n    print(f'  {bucket[\"Name\"]}')\n\n# Uploading files\ndef upload_file(file_name, bucket, object_name=None):\n    \"\"\"Upload a file to an S3 bucket\n\n    :param file_name: File to upload\n    :param bucket: Bucket to upload to\n    :param object_name: S3 object name. If not specified then file_name is used\n    :return: True if file was uploaded, else False\n    \"\"\"\n\n    # If S3 object_name was not specified, use file_name\n    if object_name is None:\n        object_name = os.path.basename(file_name)\n\n    # Upload the file\n    s3_client = boto3.client('s3')\n    try:\n        response = s3_client.upload_file(file_name, bucket, object_name)\n    except ClientError as e:\n        logging.error(e)\n        return False\n    return True\n\n\n# Downloading Homero - La Iliada book\ndef download_book():\n    url = 'https://www.gutenberg.org/cache/epub/57654/pg57654.txt'\n    os.system(f\"wget -O Homero_La_Iliada.tx {url}\")\n    \n    \nupload_file('Homero_La_Iliada.txt', 'boto3challenge')\n\n# Reading and printing txt file on S3 bucket\ndef print_file():\n    response = s3.list_objects_v2(Bucket='boto3challenge')\n    for item in response['Contents']:\n        print(item['Key'])\n\n\nprint_file()\n\n\ndef read_file():\n    response = s3.get_object(\n        Bucket='boto3challenge',\n        Key='Homero_La_Iliada.txt'\n        )\n    contents = response['Body'].read()\n    # print(f'Reading the file {response.Key}')\n    print(contents.decode(\"utf-8\"))\n    \n\nread_file()\n\n\n# s3_file = s3://boto3challenge/Homero_La_Iliada.txt\n\n# aws s3 cp s3://boto3challenge/Homero_La_Iliada.txt - | head -100\n\n# Delete objetc in s3\n# aws s3 rm s3://boto3challenge/Homero_La_Iliada.txt\n\n# Delete bucket\n# aws s3 rb s3://boto3challenge","undoManager":{"mark":-2,"position":100,"stack":[[{"start":{"row":46,"column":0},"end":{"row":46,"column":47},"action":"insert","lines":["# Output the bucket names after bucket creation"],"id":1209}],[{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"remove","lines":["r"],"id":1210},{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"remove","lines":["e"]},{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"remove","lines":["a"]},{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"remove","lines":["d"]},{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"remove","lines":["_"]},{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"remove","lines":["a"]},{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"remove","lines":["n"]},{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"remove","lines":["d"]},{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"remove","lines":["_"]}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["r"],"id":1211},{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["e"]},{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["a"]},{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["d"]},{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["_"]},{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["a"]},{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["n"]},{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["d"]},{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["_"]}],[{"start":{"row":92,"column":12},"end":{"row":93,"column":0},"action":"insert","lines":["",""],"id":1212},{"start":{"row":93,"column":0},"end":{"row":94,"column":0},"action":"insert","lines":["",""]},{"start":{"row":94,"column":0},"end":{"row":95,"column":0},"action":"insert","lines":["",""]},{"start":{"row":95,"column":0},"end":{"row":95,"column":1},"action":"insert","lines":["d"]},{"start":{"row":95,"column":1},"end":{"row":95,"column":2},"action":"insert","lines":["e"]},{"start":{"row":95,"column":2},"end":{"row":95,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":95,"column":3},"end":{"row":95,"column":4},"action":"insert","lines":[" "],"id":1213},{"start":{"row":95,"column":4},"end":{"row":95,"column":5},"action":"insert","lines":["r"]},{"start":{"row":95,"column":5},"end":{"row":95,"column":6},"action":"insert","lines":["e"]},{"start":{"row":95,"column":6},"end":{"row":95,"column":7},"action":"insert","lines":["a"]},{"start":{"row":95,"column":7},"end":{"row":95,"column":8},"action":"insert","lines":["d"]},{"start":{"row":95,"column":8},"end":{"row":95,"column":9},"action":"insert","lines":["_"]},{"start":{"row":95,"column":9},"end":{"row":95,"column":10},"action":"insert","lines":["f"]},{"start":{"row":95,"column":10},"end":{"row":95,"column":11},"action":"insert","lines":["i"]},{"start":{"row":95,"column":11},"end":{"row":95,"column":12},"action":"insert","lines":["l"]},{"start":{"row":95,"column":12},"end":{"row":95,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":95,"column":13},"end":{"row":95,"column":15},"action":"insert","lines":["()"],"id":1214}],[{"start":{"row":95,"column":15},"end":{"row":95,"column":16},"action":"insert","lines":[":"],"id":1215}],[{"start":{"row":95,"column":16},"end":{"row":96,"column":0},"action":"insert","lines":["",""],"id":1216},{"start":{"row":96,"column":0},"end":{"row":96,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":96,"column":4},"end":{"row":99,"column":1},"action":"insert","lines":["response = client.get_object(","    Bucket='examplebucket',","    Key='HappyFace.jpg',",")"],"id":1217}],[{"start":{"row":97,"column":12},"end":{"row":97,"column":25},"action":"remove","lines":["examplebucket"],"id":1218},{"start":{"row":97,"column":12},"end":{"row":97,"column":13},"action":"insert","lines":["b"]},{"start":{"row":97,"column":13},"end":{"row":97,"column":14},"action":"insert","lines":["o"]},{"start":{"row":97,"column":14},"end":{"row":97,"column":15},"action":"insert","lines":["t"]},{"start":{"row":97,"column":15},"end":{"row":97,"column":16},"action":"insert","lines":["o"]},{"start":{"row":97,"column":16},"end":{"row":97,"column":17},"action":"insert","lines":["3"]},{"start":{"row":97,"column":17},"end":{"row":97,"column":18},"action":"insert","lines":["c"]},{"start":{"row":97,"column":18},"end":{"row":97,"column":19},"action":"insert","lines":["h"]},{"start":{"row":97,"column":19},"end":{"row":97,"column":20},"action":"insert","lines":["a"]},{"start":{"row":97,"column":20},"end":{"row":97,"column":21},"action":"insert","lines":["l"]},{"start":{"row":97,"column":21},"end":{"row":97,"column":22},"action":"insert","lines":["l"]},{"start":{"row":97,"column":22},"end":{"row":97,"column":23},"action":"insert","lines":["e"]},{"start":{"row":97,"column":23},"end":{"row":97,"column":24},"action":"insert","lines":["n"]},{"start":{"row":97,"column":24},"end":{"row":97,"column":25},"action":"insert","lines":["g"]},{"start":{"row":97,"column":25},"end":{"row":97,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":98,"column":9},"end":{"row":98,"column":22},"action":"remove","lines":["HappyFace.jpg"],"id":1219},{"start":{"row":98,"column":9},"end":{"row":98,"column":10},"action":"insert","lines":["H"]},{"start":{"row":98,"column":10},"end":{"row":98,"column":11},"action":"insert","lines":["o"]},{"start":{"row":98,"column":11},"end":{"row":98,"column":12},"action":"insert","lines":["m"]},{"start":{"row":98,"column":12},"end":{"row":98,"column":13},"action":"insert","lines":["e"]},{"start":{"row":98,"column":13},"end":{"row":98,"column":14},"action":"insert","lines":["r"]},{"start":{"row":98,"column":14},"end":{"row":98,"column":15},"action":"insert","lines":["o"]},{"start":{"row":98,"column":15},"end":{"row":98,"column":16},"action":"insert","lines":["_"]}],[{"start":{"row":98,"column":9},"end":{"row":98,"column":16},"action":"remove","lines":["Homero_"],"id":1220},{"start":{"row":98,"column":9},"end":{"row":98,"column":29},"action":"insert","lines":["Homero_La_Iliada.txt"]}],[{"start":{"row":99,"column":1},"end":{"row":100,"column":0},"action":"insert","lines":["",""],"id":1221},{"start":{"row":100,"column":0},"end":{"row":101,"column":0},"action":"insert","lines":["",""]},{"start":{"row":101,"column":0},"end":{"row":102,"column":0},"action":"insert","lines":["",""]},{"start":{"row":102,"column":0},"end":{"row":102,"column":1},"action":"insert","lines":["r"]},{"start":{"row":102,"column":1},"end":{"row":102,"column":2},"action":"insert","lines":["e"]},{"start":{"row":102,"column":2},"end":{"row":102,"column":3},"action":"insert","lines":["a"]},{"start":{"row":102,"column":3},"end":{"row":102,"column":4},"action":"insert","lines":["d"]}],[{"start":{"row":102,"column":0},"end":{"row":102,"column":4},"action":"remove","lines":["read"],"id":1222},{"start":{"row":102,"column":0},"end":{"row":102,"column":11},"action":"insert","lines":["read_file()"]}],[{"start":{"row":96,"column":15},"end":{"row":96,"column":16},"action":"remove","lines":["c"],"id":1223},{"start":{"row":96,"column":15},"end":{"row":96,"column":16},"action":"remove","lines":["l"]},{"start":{"row":96,"column":15},"end":{"row":96,"column":16},"action":"remove","lines":["i"]},{"start":{"row":96,"column":15},"end":{"row":96,"column":16},"action":"remove","lines":["e"]},{"start":{"row":96,"column":15},"end":{"row":96,"column":16},"action":"remove","lines":["n"]},{"start":{"row":96,"column":15},"end":{"row":96,"column":16},"action":"remove","lines":["t"]}],[{"start":{"row":96,"column":15},"end":{"row":96,"column":16},"action":"insert","lines":["s"],"id":1224},{"start":{"row":96,"column":16},"end":{"row":96,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":96,"column":16},"end":{"row":96,"column":17},"action":"remove","lines":["e"],"id":1225}],[{"start":{"row":96,"column":16},"end":{"row":96,"column":17},"action":"insert","lines":["3"],"id":1226}],[{"start":{"row":99,"column":1},"end":{"row":100,"column":0},"action":"insert","lines":["",""],"id":1227}],[{"start":{"row":99,"column":1},"end":{"row":100,"column":0},"action":"insert","lines":["",""],"id":1228}],[{"start":{"row":96,"column":29},"end":{"row":97,"column":0},"action":"remove","lines":["",""],"id":1229},{"start":{"row":96,"column":29},"end":{"row":96,"column":30},"action":"remove","lines":[" "]},{"start":{"row":96,"column":29},"end":{"row":96,"column":30},"action":"remove","lines":[" "]},{"start":{"row":96,"column":29},"end":{"row":96,"column":30},"action":"remove","lines":[" "]},{"start":{"row":96,"column":29},"end":{"row":96,"column":30},"action":"remove","lines":[" "]}],[{"start":{"row":96,"column":53},"end":{"row":97,"column":0},"action":"remove","lines":["",""],"id":1230},{"start":{"row":96,"column":53},"end":{"row":96,"column":54},"action":"remove","lines":[" "]},{"start":{"row":96,"column":53},"end":{"row":96,"column":54},"action":"remove","lines":[" "]},{"start":{"row":96,"column":53},"end":{"row":96,"column":54},"action":"remove","lines":[" "]}],[{"start":{"row":96,"column":29},"end":{"row":97,"column":0},"action":"insert","lines":["",""],"id":1231},{"start":{"row":97,"column":0},"end":{"row":97,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":97,"column":32},"end":{"row":97,"column":33},"action":"remove","lines":[" "],"id":1232}],[{"start":{"row":97,"column":32},"end":{"row":98,"column":0},"action":"insert","lines":["",""],"id":1233},{"start":{"row":98,"column":0},"end":{"row":98,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":98,"column":35},"end":{"row":99,"column":0},"action":"remove","lines":["",""],"id":1234}],[{"start":{"row":98,"column":35},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":1235},{"start":{"row":99,"column":0},"end":{"row":99,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":99,"column":9},"end":{"row":100,"column":0},"action":"insert","lines":["",""],"id":1236},{"start":{"row":100,"column":0},"end":{"row":100,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":100,"column":4},"end":{"row":100,"column":8},"action":"remove","lines":["    "],"id":1237}],[{"start":{"row":100,"column":4},"end":{"row":100,"column":6},"action":"insert","lines":["[]"],"id":1238}],[{"start":{"row":100,"column":5},"end":{"row":100,"column":6},"action":"insert","lines":["r"],"id":1239},{"start":{"row":100,"column":6},"end":{"row":100,"column":7},"action":"insert","lines":["i"]},{"start":{"row":100,"column":7},"end":{"row":100,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":100,"column":7},"end":{"row":100,"column":8},"action":"remove","lines":["m"],"id":1240},{"start":{"row":100,"column":6},"end":{"row":100,"column":7},"action":"remove","lines":["i"]},{"start":{"row":100,"column":5},"end":{"row":100,"column":6},"action":"remove","lines":["r"]},{"start":{"row":100,"column":4},"end":{"row":100,"column":6},"action":"remove","lines":["[]"]}],[{"start":{"row":100,"column":4},"end":{"row":100,"column":5},"action":"insert","lines":["p"],"id":1241},{"start":{"row":100,"column":5},"end":{"row":100,"column":6},"action":"insert","lines":["r"]},{"start":{"row":100,"column":6},"end":{"row":100,"column":7},"action":"insert","lines":["n"]},{"start":{"row":100,"column":7},"end":{"row":100,"column":8},"action":"insert","lines":["t"]}],[{"start":{"row":100,"column":7},"end":{"row":100,"column":8},"action":"remove","lines":["t"],"id":1242},{"start":{"row":100,"column":6},"end":{"row":100,"column":7},"action":"remove","lines":["n"]}],[{"start":{"row":100,"column":6},"end":{"row":100,"column":7},"action":"insert","lines":["i"],"id":1243},{"start":{"row":100,"column":7},"end":{"row":100,"column":8},"action":"insert","lines":["n"]},{"start":{"row":100,"column":8},"end":{"row":100,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":100,"column":9},"end":{"row":100,"column":11},"action":"insert","lines":["()"],"id":1244}],[{"start":{"row":100,"column":10},"end":{"row":100,"column":11},"action":"insert","lines":["r"],"id":1245},{"start":{"row":100,"column":11},"end":{"row":100,"column":12},"action":"insert","lines":["e"]},{"start":{"row":100,"column":12},"end":{"row":100,"column":13},"action":"insert","lines":["s"]},{"start":{"row":100,"column":13},"end":{"row":100,"column":14},"action":"insert","lines":["p"]},{"start":{"row":100,"column":14},"end":{"row":100,"column":15},"action":"insert","lines":["o"]},{"start":{"row":100,"column":15},"end":{"row":100,"column":16},"action":"insert","lines":["n"]},{"start":{"row":100,"column":16},"end":{"row":100,"column":17},"action":"insert","lines":["s"]},{"start":{"row":100,"column":17},"end":{"row":100,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":101,"column":0},"end":{"row":102,"column":0},"action":"insert","lines":["",""],"id":1246},{"start":{"row":102,"column":0},"end":{"row":103,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":103,"column":0},"end":{"row":105,"column":35},"action":"insert","lines":[" data = s3.get_object(Bucket=bucket, Key=o.get('Key'))","    contents = data['Body'].read()","    print(contents.decode(\"utf-8\"))"],"id":1247}],[{"start":{"row":98,"column":35},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":1248},{"start":{"row":99,"column":0},"end":{"row":99,"column":8},"action":"insert","lines":["        "]},{"start":{"row":99,"column":8},"end":{"row":99,"column":9},"action":"insert","lines":["c"]},{"start":{"row":99,"column":9},"end":{"row":99,"column":10},"action":"insert","lines":["p"]},{"start":{"row":99,"column":10},"end":{"row":99,"column":11},"action":"insert","lines":["m"]},{"start":{"row":99,"column":11},"end":{"row":99,"column":12},"action":"insert","lines":["t"]},{"start":{"row":99,"column":12},"end":{"row":99,"column":13},"action":"insert","lines":["e"]},{"start":{"row":99,"column":13},"end":{"row":99,"column":14},"action":"insert","lines":["m"]}],[{"start":{"row":99,"column":13},"end":{"row":99,"column":14},"action":"remove","lines":["m"],"id":1249},{"start":{"row":99,"column":12},"end":{"row":99,"column":13},"action":"remove","lines":["e"]},{"start":{"row":99,"column":11},"end":{"row":99,"column":12},"action":"remove","lines":["t"]},{"start":{"row":99,"column":10},"end":{"row":99,"column":11},"action":"remove","lines":["m"]},{"start":{"row":99,"column":9},"end":{"row":99,"column":10},"action":"remove","lines":["p"]}],[{"start":{"row":99,"column":9},"end":{"row":99,"column":10},"action":"insert","lines":["c"],"id":1250},{"start":{"row":99,"column":10},"end":{"row":99,"column":11},"action":"insert","lines":["o"]}],[{"start":{"row":99,"column":10},"end":{"row":99,"column":11},"action":"remove","lines":["o"],"id":1251},{"start":{"row":99,"column":9},"end":{"row":99,"column":10},"action":"remove","lines":["c"]}],[{"start":{"row":99,"column":9},"end":{"row":99,"column":10},"action":"insert","lines":["o"],"id":1252},{"start":{"row":99,"column":10},"end":{"row":99,"column":11},"action":"insert","lines":["n"]},{"start":{"row":99,"column":11},"end":{"row":99,"column":12},"action":"insert","lines":["t"]},{"start":{"row":99,"column":12},"end":{"row":99,"column":13},"action":"insert","lines":["e"]},{"start":{"row":99,"column":13},"end":{"row":99,"column":14},"action":"insert","lines":["n"]},{"start":{"row":99,"column":14},"end":{"row":99,"column":15},"action":"insert","lines":["t"]},{"start":{"row":99,"column":15},"end":{"row":99,"column":16},"action":"insert","lines":["s"]}],[{"start":{"row":99,"column":16},"end":{"row":99,"column":17},"action":"insert","lines":[" "],"id":1253},{"start":{"row":99,"column":17},"end":{"row":99,"column":18},"action":"insert","lines":["="]}],[{"start":{"row":99,"column":18},"end":{"row":99,"column":19},"action":"insert","lines":[" "],"id":1254},{"start":{"row":99,"column":19},"end":{"row":99,"column":20},"action":"insert","lines":["d"]},{"start":{"row":99,"column":20},"end":{"row":99,"column":21},"action":"insert","lines":["a"]},{"start":{"row":99,"column":21},"end":{"row":99,"column":22},"action":"insert","lines":["t"]},{"start":{"row":99,"column":22},"end":{"row":99,"column":23},"action":"insert","lines":["a"]}],[{"start":{"row":99,"column":23},"end":{"row":99,"column":25},"action":"insert","lines":["[]"],"id":1255}],[{"start":{"row":99,"column":23},"end":{"row":99,"column":25},"action":"remove","lines":["[]"],"id":1256},{"start":{"row":99,"column":22},"end":{"row":99,"column":23},"action":"remove","lines":["a"]},{"start":{"row":99,"column":21},"end":{"row":99,"column":22},"action":"remove","lines":["t"]},{"start":{"row":99,"column":20},"end":{"row":99,"column":21},"action":"remove","lines":["a"]},{"start":{"row":99,"column":19},"end":{"row":99,"column":20},"action":"remove","lines":["d"]},{"start":{"row":99,"column":18},"end":{"row":99,"column":19},"action":"remove","lines":[" "]},{"start":{"row":99,"column":17},"end":{"row":99,"column":18},"action":"remove","lines":["="]},{"start":{"row":99,"column":16},"end":{"row":99,"column":17},"action":"remove","lines":[" "]},{"start":{"row":99,"column":15},"end":{"row":99,"column":16},"action":"remove","lines":["s"]},{"start":{"row":99,"column":14},"end":{"row":99,"column":15},"action":"remove","lines":["t"]},{"start":{"row":99,"column":13},"end":{"row":99,"column":14},"action":"remove","lines":["n"]},{"start":{"row":99,"column":12},"end":{"row":99,"column":13},"action":"remove","lines":["e"]},{"start":{"row":99,"column":11},"end":{"row":99,"column":12},"action":"remove","lines":["t"]},{"start":{"row":99,"column":10},"end":{"row":99,"column":11},"action":"remove","lines":["n"]},{"start":{"row":99,"column":9},"end":{"row":99,"column":10},"action":"remove","lines":["o"]}],[{"start":{"row":99,"column":8},"end":{"row":99,"column":9},"action":"remove","lines":["c"],"id":1257},{"start":{"row":99,"column":4},"end":{"row":99,"column":8},"action":"remove","lines":["    "]},{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"remove","lines":["    "]},{"start":{"row":98,"column":35},"end":{"row":99,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":98,"column":35},"end":{"row":99,"column":0},"action":"remove","lines":["",""],"id":1258},{"start":{"row":98,"column":35},"end":{"row":98,"column":36},"action":"remove","lines":[" "]},{"start":{"row":98,"column":35},"end":{"row":98,"column":36},"action":"remove","lines":[" "]},{"start":{"row":98,"column":35},"end":{"row":98,"column":36},"action":"remove","lines":[" "]},{"start":{"row":98,"column":35},"end":{"row":98,"column":36},"action":"remove","lines":[" "]},{"start":{"row":98,"column":35},"end":{"row":98,"column":36},"action":"remove","lines":[" "]},{"start":{"row":98,"column":35},"end":{"row":98,"column":36},"action":"remove","lines":[" "]},{"start":{"row":98,"column":35},"end":{"row":98,"column":36},"action":"remove","lines":[" "]}],[{"start":{"row":98,"column":35},"end":{"row":98,"column":36},"action":"remove","lines":[" "],"id":1259}],[{"start":{"row":98,"column":34},"end":{"row":98,"column":35},"action":"remove","lines":[","],"id":1260}],[{"start":{"row":98,"column":34},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":1261},{"start":{"row":99,"column":0},"end":{"row":99,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":99,"column":9},"end":{"row":100,"column":0},"action":"insert","lines":["",""],"id":1262},{"start":{"row":100,"column":0},"end":{"row":100,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":100,"column":4},"end":{"row":100,"column":8},"action":"remove","lines":["    "],"id":1263}],[{"start":{"row":100,"column":4},"end":{"row":100,"column":5},"action":"insert","lines":["c"],"id":1264},{"start":{"row":100,"column":5},"end":{"row":100,"column":6},"action":"insert","lines":["o"]},{"start":{"row":100,"column":6},"end":{"row":100,"column":7},"action":"insert","lines":["n"]},{"start":{"row":100,"column":7},"end":{"row":100,"column":8},"action":"insert","lines":["t"]},{"start":{"row":100,"column":8},"end":{"row":100,"column":9},"action":"insert","lines":["e"]},{"start":{"row":100,"column":9},"end":{"row":100,"column":10},"action":"insert","lines":["n"]},{"start":{"row":100,"column":10},"end":{"row":100,"column":11},"action":"insert","lines":["t"]},{"start":{"row":100,"column":11},"end":{"row":100,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":100,"column":12},"end":{"row":100,"column":13},"action":"insert","lines":[" "],"id":1265},{"start":{"row":100,"column":13},"end":{"row":100,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":100,"column":14},"end":{"row":100,"column":15},"action":"insert","lines":[" "],"id":1266},{"start":{"row":100,"column":15},"end":{"row":100,"column":16},"action":"insert","lines":["d"]},{"start":{"row":100,"column":16},"end":{"row":100,"column":17},"action":"insert","lines":["a"]},{"start":{"row":100,"column":17},"end":{"row":100,"column":18},"action":"insert","lines":["t"]},{"start":{"row":100,"column":18},"end":{"row":100,"column":19},"action":"insert","lines":["a"]}],[{"start":{"row":100,"column":18},"end":{"row":100,"column":19},"action":"remove","lines":["a"],"id":1267},{"start":{"row":100,"column":17},"end":{"row":100,"column":18},"action":"remove","lines":["t"]},{"start":{"row":100,"column":16},"end":{"row":100,"column":17},"action":"remove","lines":["a"]},{"start":{"row":100,"column":15},"end":{"row":100,"column":16},"action":"remove","lines":["d"]}],[{"start":{"row":100,"column":15},"end":{"row":100,"column":16},"action":"insert","lines":["r"],"id":1268},{"start":{"row":100,"column":16},"end":{"row":100,"column":17},"action":"insert","lines":["e"]},{"start":{"row":100,"column":17},"end":{"row":100,"column":18},"action":"insert","lines":["s"]},{"start":{"row":100,"column":18},"end":{"row":100,"column":19},"action":"insert","lines":["p"]},{"start":{"row":100,"column":19},"end":{"row":100,"column":20},"action":"insert","lines":["o"]},{"start":{"row":100,"column":20},"end":{"row":100,"column":21},"action":"insert","lines":["j"]},{"start":{"row":100,"column":21},"end":{"row":100,"column":22},"action":"insert","lines":["s"]},{"start":{"row":100,"column":22},"end":{"row":100,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":100,"column":22},"end":{"row":100,"column":23},"action":"remove","lines":["e"],"id":1269},{"start":{"row":100,"column":21},"end":{"row":100,"column":22},"action":"remove","lines":["s"]},{"start":{"row":100,"column":20},"end":{"row":100,"column":21},"action":"remove","lines":["j"]}],[{"start":{"row":100,"column":20},"end":{"row":100,"column":21},"action":"insert","lines":["n"],"id":1270},{"start":{"row":100,"column":21},"end":{"row":100,"column":22},"action":"insert","lines":["s"]},{"start":{"row":100,"column":22},"end":{"row":100,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":100,"column":23},"end":{"row":100,"column":25},"action":"insert","lines":["[]"],"id":1271}],[{"start":{"row":100,"column":24},"end":{"row":100,"column":26},"action":"insert","lines":["''"],"id":1272}],[{"start":{"row":100,"column":25},"end":{"row":100,"column":26},"action":"insert","lines":["D"],"id":1273},{"start":{"row":100,"column":26},"end":{"row":100,"column":27},"action":"insert","lines":["o"]},{"start":{"row":100,"column":27},"end":{"row":100,"column":28},"action":"insert","lines":["d"]},{"start":{"row":100,"column":28},"end":{"row":100,"column":29},"action":"insert","lines":["y"]}],[{"start":{"row":100,"column":28},"end":{"row":100,"column":29},"action":"remove","lines":["y"],"id":1274},{"start":{"row":100,"column":27},"end":{"row":100,"column":28},"action":"remove","lines":["d"]},{"start":{"row":100,"column":26},"end":{"row":100,"column":27},"action":"remove","lines":["o"]},{"start":{"row":100,"column":25},"end":{"row":100,"column":26},"action":"remove","lines":["D"]}],[{"start":{"row":100,"column":25},"end":{"row":100,"column":26},"action":"insert","lines":["B"],"id":1275},{"start":{"row":100,"column":26},"end":{"row":100,"column":27},"action":"insert","lines":["o"]},{"start":{"row":100,"column":27},"end":{"row":100,"column":28},"action":"insert","lines":["d"]},{"start":{"row":100,"column":28},"end":{"row":100,"column":29},"action":"insert","lines":["y"]}],[{"start":{"row":100,"column":31},"end":{"row":100,"column":32},"action":"insert","lines":["."],"id":1276},{"start":{"row":100,"column":32},"end":{"row":100,"column":33},"action":"insert","lines":["r"]},{"start":{"row":100,"column":33},"end":{"row":100,"column":34},"action":"insert","lines":["e"]},{"start":{"row":100,"column":34},"end":{"row":100,"column":35},"action":"insert","lines":["a"]},{"start":{"row":100,"column":35},"end":{"row":100,"column":36},"action":"insert","lines":["d"]}],[{"start":{"row":100,"column":36},"end":{"row":100,"column":38},"action":"insert","lines":["()"],"id":1277}],[{"start":{"row":101,"column":17},"end":{"row":101,"column":18},"action":"remove","lines":["e"],"id":1278},{"start":{"row":101,"column":16},"end":{"row":101,"column":17},"action":"remove","lines":["s"]},{"start":{"row":101,"column":15},"end":{"row":101,"column":16},"action":"remove","lines":["n"]},{"start":{"row":101,"column":14},"end":{"row":101,"column":15},"action":"remove","lines":["o"]},{"start":{"row":101,"column":13},"end":{"row":101,"column":14},"action":"remove","lines":["p"]},{"start":{"row":101,"column":12},"end":{"row":101,"column":13},"action":"remove","lines":["s"]},{"start":{"row":101,"column":11},"end":{"row":101,"column":12},"action":"remove","lines":["e"]},{"start":{"row":101,"column":10},"end":{"row":101,"column":11},"action":"remove","lines":["r"]}],[{"start":{"row":101,"column":10},"end":{"row":101,"column":11},"action":"insert","lines":["c"],"id":1279},{"start":{"row":101,"column":11},"end":{"row":101,"column":12},"action":"insert","lines":["o"]},{"start":{"row":101,"column":12},"end":{"row":101,"column":13},"action":"insert","lines":["n"]},{"start":{"row":101,"column":13},"end":{"row":101,"column":14},"action":"insert","lines":["t"]},{"start":{"row":101,"column":14},"end":{"row":101,"column":15},"action":"insert","lines":["e"]},{"start":{"row":101,"column":15},"end":{"row":101,"column":16},"action":"insert","lines":["n"]},{"start":{"row":101,"column":16},"end":{"row":101,"column":17},"action":"insert","lines":["s"]},{"start":{"row":101,"column":17},"end":{"row":101,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":101,"column":17},"end":{"row":101,"column":18},"action":"remove","lines":["t"],"id":1280},{"start":{"row":101,"column":16},"end":{"row":101,"column":17},"action":"remove","lines":["s"]}],[{"start":{"row":101,"column":16},"end":{"row":101,"column":17},"action":"insert","lines":["t"],"id":1281},{"start":{"row":101,"column":17},"end":{"row":101,"column":18},"action":"insert","lines":["s"]},{"start":{"row":101,"column":18},"end":{"row":101,"column":19},"action":"insert","lines":["."]},{"start":{"row":101,"column":19},"end":{"row":101,"column":20},"action":"insert","lines":["d"]},{"start":{"row":101,"column":20},"end":{"row":101,"column":21},"action":"insert","lines":["e"]},{"start":{"row":101,"column":21},"end":{"row":101,"column":22},"action":"insert","lines":["c"]},{"start":{"row":101,"column":22},"end":{"row":101,"column":23},"action":"insert","lines":["o"]},{"start":{"row":101,"column":23},"end":{"row":101,"column":24},"action":"insert","lines":["d"]},{"start":{"row":101,"column":24},"end":{"row":101,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":101,"column":25},"end":{"row":101,"column":27},"action":"insert","lines":["()"],"id":1282}],[{"start":{"row":101,"column":26},"end":{"row":101,"column":28},"action":"insert","lines":["\"\""],"id":1283}],[{"start":{"row":101,"column":27},"end":{"row":101,"column":28},"action":"insert","lines":["u"],"id":1284},{"start":{"row":101,"column":28},"end":{"row":101,"column":29},"action":"insert","lines":["t"]},{"start":{"row":101,"column":29},"end":{"row":101,"column":30},"action":"insert","lines":["d"]}],[{"start":{"row":101,"column":29},"end":{"row":101,"column":30},"action":"remove","lines":["d"],"id":1285}],[{"start":{"row":101,"column":29},"end":{"row":101,"column":30},"action":"insert","lines":["f"],"id":1286},{"start":{"row":101,"column":30},"end":{"row":101,"column":31},"action":"insert","lines":["-"]},{"start":{"row":101,"column":31},"end":{"row":101,"column":32},"action":"insert","lines":["8"]}],[{"start":{"row":104,"column":32},"end":{"row":106,"column":32},"action":"remove","lines":["ket, Key=o.get('Key'))","    contents = data['Body'].read()","    print(contents.decode(\"utf-8"],"id":1287}],[{"start":{"row":104,"column":0},"end":{"row":104,"column":35},"action":"remove","lines":[" data = s3.get_object(Bucket=buc\"))"],"id":1288},{"start":{"row":104,"column":0},"end":{"row":105,"column":0},"action":"remove","lines":["",""]},{"start":{"row":104,"column":0},"end":{"row":105,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":103,"column":0},"end":{"row":104,"column":0},"action":"remove","lines":["",""],"id":1289},{"start":{"row":102,"column":0},"end":{"row":103,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":101,"column":35},"end":{"row":102,"column":0},"action":"remove","lines":["",""],"id":1290},{"start":{"row":101,"column":35},"end":{"row":102,"column":0},"action":"insert","lines":["",""]},{"start":{"row":102,"column":0},"end":{"row":102,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":101,"column":4},"end":{"row":102,"column":0},"action":"insert","lines":["",""],"id":1291},{"start":{"row":102,"column":0},"end":{"row":102,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":101,"column":4},"end":{"row":101,"column":5},"action":"insert","lines":["p"],"id":1292},{"start":{"row":101,"column":5},"end":{"row":101,"column":6},"action":"insert","lines":["r"]},{"start":{"row":101,"column":6},"end":{"row":101,"column":7},"action":"insert","lines":["u"]},{"start":{"row":101,"column":7},"end":{"row":101,"column":8},"action":"insert","lines":["n"]},{"start":{"row":101,"column":8},"end":{"row":101,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":101,"column":8},"end":{"row":101,"column":9},"action":"remove","lines":["t"],"id":1293},{"start":{"row":101,"column":7},"end":{"row":101,"column":8},"action":"remove","lines":["n"]},{"start":{"row":101,"column":6},"end":{"row":101,"column":7},"action":"remove","lines":["u"]}],[{"start":{"row":101,"column":6},"end":{"row":101,"column":7},"action":"insert","lines":["i"],"id":1294},{"start":{"row":101,"column":7},"end":{"row":101,"column":8},"action":"insert","lines":["m"]},{"start":{"row":101,"column":8},"end":{"row":101,"column":9},"action":"insert","lines":["n"]},{"start":{"row":101,"column":9},"end":{"row":101,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":101,"column":9},"end":{"row":101,"column":10},"action":"remove","lines":["t"],"id":1295},{"start":{"row":101,"column":8},"end":{"row":101,"column":9},"action":"remove","lines":["n"]},{"start":{"row":101,"column":7},"end":{"row":101,"column":8},"action":"remove","lines":["m"]}],[{"start":{"row":101,"column":7},"end":{"row":101,"column":8},"action":"insert","lines":["n"],"id":1296},{"start":{"row":101,"column":8},"end":{"row":101,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":101,"column":9},"end":{"row":101,"column":11},"action":"insert","lines":["()"],"id":1297}],[{"start":{"row":101,"column":10},"end":{"row":101,"column":11},"action":"insert","lines":["f"],"id":1298}],[{"start":{"row":101,"column":11},"end":{"row":101,"column":13},"action":"insert","lines":["''"],"id":1299}],[{"start":{"row":101,"column":12},"end":{"row":101,"column":13},"action":"insert","lines":["R"],"id":1300},{"start":{"row":101,"column":13},"end":{"row":101,"column":14},"action":"insert","lines":["e"]},{"start":{"row":101,"column":14},"end":{"row":101,"column":15},"action":"insert","lines":["a"]},{"start":{"row":101,"column":15},"end":{"row":101,"column":16},"action":"insert","lines":["d"]},{"start":{"row":101,"column":16},"end":{"row":101,"column":17},"action":"insert","lines":["i"]},{"start":{"row":101,"column":17},"end":{"row":101,"column":18},"action":"insert","lines":["n"]},{"start":{"row":101,"column":18},"end":{"row":101,"column":19},"action":"insert","lines":["g"]}],[{"start":{"row":101,"column":19},"end":{"row":101,"column":20},"action":"insert","lines":[" "],"id":1301},{"start":{"row":101,"column":20},"end":{"row":101,"column":21},"action":"insert","lines":["t"]},{"start":{"row":101,"column":21},"end":{"row":101,"column":22},"action":"insert","lines":["h"]},{"start":{"row":101,"column":22},"end":{"row":101,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":101,"column":23},"end":{"row":101,"column":24},"action":"insert","lines":[" "],"id":1302},{"start":{"row":101,"column":24},"end":{"row":101,"column":25},"action":"insert","lines":["d"]},{"start":{"row":101,"column":25},"end":{"row":101,"column":26},"action":"insert","lines":["i"]}],[{"start":{"row":101,"column":25},"end":{"row":101,"column":26},"action":"remove","lines":["i"],"id":1303},{"start":{"row":101,"column":24},"end":{"row":101,"column":25},"action":"remove","lines":["d"]}],[{"start":{"row":101,"column":24},"end":{"row":101,"column":25},"action":"insert","lines":["f"],"id":1304},{"start":{"row":101,"column":25},"end":{"row":101,"column":26},"action":"insert","lines":["i"]},{"start":{"row":101,"column":26},"end":{"row":101,"column":27},"action":"insert","lines":["l"]},{"start":{"row":101,"column":27},"end":{"row":101,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":101,"column":28},"end":{"row":101,"column":29},"action":"insert","lines":[" "],"id":1305},{"start":{"row":101,"column":29},"end":{"row":101,"column":30},"action":"insert","lines":["{"]},{"start":{"row":101,"column":30},"end":{"row":101,"column":31},"action":"insert","lines":["}"]}],[{"start":{"row":101,"column":30},"end":{"row":101,"column":31},"action":"insert","lines":["K"],"id":1306},{"start":{"row":101,"column":31},"end":{"row":101,"column":32},"action":"insert","lines":["e"]},{"start":{"row":101,"column":32},"end":{"row":101,"column":33},"action":"insert","lines":["y"]}],[{"start":{"row":101,"column":30},"end":{"row":101,"column":31},"action":"insert","lines":["r"],"id":1307},{"start":{"row":101,"column":31},"end":{"row":101,"column":32},"action":"insert","lines":["e"]},{"start":{"row":101,"column":32},"end":{"row":101,"column":33},"action":"insert","lines":["s"]},{"start":{"row":101,"column":33},"end":{"row":101,"column":34},"action":"insert","lines":["p"]},{"start":{"row":101,"column":34},"end":{"row":101,"column":35},"action":"insert","lines":["o"]},{"start":{"row":101,"column":35},"end":{"row":101,"column":36},"action":"insert","lines":["n"]},{"start":{"row":101,"column":36},"end":{"row":101,"column":37},"action":"insert","lines":["s"]},{"start":{"row":101,"column":37},"end":{"row":101,"column":38},"action":"insert","lines":["e"]}],[{"start":{"row":101,"column":38},"end":{"row":101,"column":39},"action":"insert","lines":["."],"id":1308}],[{"start":{"row":101,"column":4},"end":{"row":101,"column":6},"action":"insert","lines":["# "],"id":1309}]]},"ace":{"folds":[],"scrolltop":1078,"scrollleft":0,"selection":{"start":{"row":113,"column":0},"end":{"row":114,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":88,"state":"start","mode":"ace/mode/python"}},"timestamp":1698722132605}