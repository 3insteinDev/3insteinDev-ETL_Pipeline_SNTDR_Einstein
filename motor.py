#********************************************************************
#**************************EXTRACT***********************************
import pandas as pd
import json

#-----------extraindo do arquivo csv a lista de ID--------------------
df = pd.read_csv(r'ETL_Pipeline_SNTDR_Einstein\SDW2023.csv', encoding='utf-8')
user_ids = df['UserID'].tolist()
print(user_ids)

#-----------acessando o meu banco de dados, neste caso estou usando umarquivo json 
# para simplificar este exercício-------------------------------------------------
with open(r'ETL_Pipeline_SNTDR_Einstein\usuarios.json', 'r', encoding='utf-8') as file:
	users = json.load(file)

def get_user(id):
    for user in users:
        if user['id'] == id:
            return user
    return None

selected_users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(selected_users, indent=2))


# #********************************************************************
# #**************************TRANSFORM*********************************
def update_user(user, message):
    if 'news' not in user:
        user['news'] = []
    user['news'].append(message)

#inserindo uma msg que deve ser enviada ao usuário na data do seu niver
#diferente do chatgpt, aqui será inserida uma msg padronizada a todos os usuários contidos na lista de id
for user in users:
    if user['id'] in user_ids:
        message = {
            "id": 280,
            "icon": "ETL_Pipeline_SNTDR_Einstein\\bolo.niver.jpg",
            "description": f"Parabéns {user['name']} pelo seu aniversário! Desejamos a você um dia repleto de alegria e sucesso. 🎉🎂"
        }
        update_user(user, message)

# #********************************************************************
# #**************************LOAD**************************************

# Imprimindo os usuários com a mensagem de aniversário adicionada
print(json.dumps(selected_users, indent=2))


# Salvando os usuários com o novo conteúdo----------------------------
with open(r'ETL_Pipeline_SNTDR_Einstein\usuarios.json', 'w', encoding='utf-8') as file:
    json.dump(users, file, indent=2, ensure_ascii=False)

print("Informações atualizadas gravadas no arquivo usuarios.json.")