import json


# 1 JSON Dosyasını Oku
def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# 2 Aynı Kullanıcının Eklenmesini Önleyerek JSON Dosyasına Yeni Kullanıcı Ekle
def add_user(file_path, name, age):
    data = read_json(file_path)  # Mevcut JSON verisini oku
    new_user = {"name": name, "age": age}

    # Kullanıcı daha önce eklenmiş mi kontrol et
    for user in data["users"]:
        if user["name"] == name and user["age"] == age:
            print(f" {name} ({age}) zaten listede!")
            return  # Fonksiyonu burada sonlandır

    data["users"].append(new_user)  # Yeni kullanıcı ekle

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)  # Güncellenmiş veriyi kaydet

    print(f" Kullanıcı eklendi: {name}, {age}")


# 3️ JSON İçeriğini Ekrana Yazdır
def print_users(file_path):
    data = read_json(file_path)
    print("\n Kullanıcı Listesi:")
    for user in data["users"]:
        print(f"- {user['name']} ({user['age']} yaşında)")


#  Fonksiyonları Çalıştır
json_file = "data.json"

print_users(json_file)  # Mevcut kullanıcıları göster
add_user(json_file, "Mehmet", 28)  # Mehmet'i tekrar eklemeyi dene
print_users(json_file)  # Güncellenmiş listeyi göster
