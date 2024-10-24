import boto3

boto3.setup_default_session(
    aws_access_key_id='ASIA2MNVMGWNR5V3OVJC',
    aws_secret_access_key='X2GiHkG03Wi9KjeTN0TdHx3ZGyD2zBWLkgwo1u/E',
    aws_session_token='IQoJb3JpZ2luX2VjEFUaCXVzLWVhc3QtMSJHMEUCIQC82PtWHVhQvadqpyt3V3DSS1P0Hr8XUsYI0dpMeS9SQQIgQNHmKRB9PxHWxp2b+WM2iJ4GujVivYxvhWSEJDElIHYqpAMIvv//////////ARAAGgw3MTM4ODE4MjY3MTUiDKxbq0AUdzlh3KU78Cr4Aq/fbl8iUWr/Yxd3DvbVb2o+ihzG/p4qI4etM17+orLFzL0kVshzWgir4ogTvwrofWuFLLvYsW6FI2c6k6vlTav26vnWsTAQVN4N0U5Zy5ONasyoYBikboRx7oJwhB2YJKXU67sP+yNfdT2+azxLVwFv1LWKNtHtss/pjLBIveAa7JCGiVfi4PJvbQUZbCaHCmBnj9ztvQYAq0cL2Xky0RtndWx+Me9QHPBsZzeCHrZ1sKGC0pm3eo5wtFEpQTn7ojMWsbi9AkjjRcl+C9kofPl2TLneXfY7l39ZXG8eq/+1DVVdu9WQ0jyktRXsd5/RyaxMSJ2cDTZvzBHwf9HEAUI7Npe0o1V4H2OQacE8MgrHJ6MPs2OfCnrVBgQ4my9OqMzzFkkVMjUtf400fPbecY7rK2qzKYSUxksJWr6+rBOyQKzJoSPsQjOcQhP9gQAkfhV53q/4dxYxV+SlEp4tmB0Zi2vh+qkCFkVpWvTlIe2ypdHpDJpfdvMw3tXjuAY6pgGhqzs4dtqLnKBsEiTS1xJlsb0R65GV6NdfPEYFtFqqokVyxX2eOk3sJizcGG3Ghg87qOZmTQpJzz5FyRVzYAEaXhS/PpT021taXI7IesiAAt3dGPRkZzTAITNoYxeIfmPH9vVmatQ63L8FGMGWLUzUCYCW5OVEfxsOMfMeRv0nb2iaOeyIT3Hrs6tAoVx0jUI51RCd8nwVoKws5ibe400BUfyMSWkI')

# criar um cliente
s3 = boto3.resource('s3')
# nome do bucket
nome_bucket = 'sprint5weber'
# criando bucket
s3.create_bucket(Bucket=nome_bucket)
arquivo = 'dados.csv'

# Nome do arquivo no bucket
nome_arquivo = 'dados.csv'

# fazer upaload para o bucket
s3.Bucket(nome_bucket).upload_file(arquivo, nome_arquivo)

print(f'Arquivo{nome_arquivo}\
    enviando para backet {nome_bucket} com sucesso!')
