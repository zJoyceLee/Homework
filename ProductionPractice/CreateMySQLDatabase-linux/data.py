import MySQLdb
import hashlib
import random

def execSQL(ss):
    print(ss)
    try:
        cursor.execute(ss)
        db.commit()
        print('commit...')
    except:
        db.rollback()
        print('rollback...')

db = MySQLdb.connect("localhost", "root", "1", "shoppingSystem", charset="utf8")
cursor = db.cursor()

print("\ninsert into User:")
users = {'liuziying':'18717810000', 'lishu':'15618130000', 'liyuzhe': '18717890000'}
for user in users.keys():
    password = user
    md5 = hashlib.md5()
    md5.update(password.encode())
    password_md5 = md5.hexdigest()
    phone = users.get(user)
    ss = """
    INSERT INTO User(username, password, phone, email, addr) VALUES(
    '{0}', '{1}', '{2}', 'testShoppingSystem@yeah.net', '上海市宝山区上大路99号上海大学'
    );
    """.format(user, password_md5, phone)
    execSQL(ss)

print("\ninsert into Commodity:")
commodity_ids = ['ILCE7SM2','ILCE7A72','ILCE7A71']
commodity_names = [
    'Sony/索尼 ILCE-7SM2 A7SM2 A7S2 微单 全画幅 相机 感光利器 五轴防抖 4K内录 最高ISO 409600',
    'Sony/索尼 ILCE-7(FE24-240mm) A7 全画幅微单套装 一镜走天下',
    'Sony/索尼 ILCE-7 A7 全画幅微单相机 2430万 像素 混合 自动对焦'
]
commodity_prices = [24179, 11598, 12979]
commodity_info = [
    """
    <table border="0" cellpadding="1" cellspacing="1" style="width:100%">
        <tbody>
                <tr>
                        <td>产品名称：Sony/索尼 ILCE-7SM2单机</td>
                        <td>品牌: Sony/索尼</td>
                        <td>像素: 约 1220万有效像素</td>
                </tr>
                <tr>
                        <td>上市时间: 2015年</td>
                        <td>传感器尺寸: 约 35.6x23.8mm（35mm全画幅）</td>
                        <td>感光元件类型: Exmor CMOS</td>
                </tr>
        </tbody>
    </table>
    """,
    """
    <table border="0" cellpadding="1" cellspacing="1" style="width:100%">
        <tbody>
                <tr>
                        <td>品牌: Sony/索尼</td>
                        <td>像素: 约 2430万</td>
                        <td>有效像素传感器尺寸: 约 35.8x23.9mm</td>
                </tr>
        </tbody>
    </table>
    """,
    """
    <table border="0" cellpadding="1" cellspacing="1" style="width:100%">
        <tbody>
                <tr>
                        <td>产品名称：Sony/索尼</td>
                        <td>ILCE-7单机品牌: Sony/索尼</td>
                        <td>像素: 约 2430万有效像素</td>
                </tr>
                <tr>
                        <td>上市时间: 2013年</td>
                        <td>传感器尺寸: 约 35.8x23.9mm</td>
                        <td>感光元件类型: CMOS</td>
                </tr>
                <tr>
                        <td>存储类型: MS卡 SD卡</td>
                        <td>闪光灯及附件类型: 外接闪光灯</td>
                        <td>快门类型: 电子快门</td>
                </tr>
        </tbody>
    </table>
    """
]
for i, commodity_id in enumerate(commodity_ids):
    ss = """
    INSERT INTO Commodity(id, name, price, info) VALUES (
    '{0}', '{1}', {2}, '{3}'
    );
    """.format(
        commodity_id,
        commodity_names[i],
        commodity_prices[i],
        commodity_info[i]
    )
    execSQL(ss)


print("\ninsert into Image:")
commodity_ids = ['ILCE7SM2','ILCE7A72','ILCE7A71']
image_for_ILCE7SM2 = [
    'SonyILCE-7SM2A7SM2A7S2_1.jpg',
    'SonyILCE-7SM2A7SM2A7S2_2.png',
    'SonyILCE-7SM2A7SM2A7S2_3.png'
]
for img_path in image_for_ILCE7SM2:
    # "{% static 'online/image/{}' %}"
    ss = """
    INSERT INTO Image(commodity_id, img_path) VALUES (
    'ILCE7SM2', '{}');
    """.format(img_path)
    execSQL(ss)
image_for_ILCE7A72 = [
    'SonyLCE-7(FE24-240mm)A7_1.jpg',
    'SonyLCE-7(FE24-240mm)A7_2.png',
    'SonyLCE-7(FE24-240mm)A7_3.png'
]
for img_path in image_for_ILCE7A72:
    ss = """
    INSERT INTO Image(commodity_id, img_path) VALUES (
    'ILCE7A72', '{}');
    """.format(img_path)
    execSQL(ss)
image_for_ILCE7A71 = [
    'SonyILCE-7A7_1.jpg',
    'SonyILCE-7A7_2.png',
    'SonyILCE-7A7_3.png'
]
for img_path in image_for_ILCE7A71:
    ss = """
    INSERT INTO Image(commodity_id, img_path) VALUES (
    'ILCE7A71', '{}');
    """.format(img_path)
    execSQL(ss)
