import MySQLdb
import hashlib
import random

def execSQL(ss):
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
                        <td>1</td>
                        <td>2</td>
                        <td>3</td>
                </tr>
                <tr>
                        <td>4</td>
                        <td>5</td>
                        <td>6</td>
                </tr>
        </tbody>
    </table>
    """,
    """
    <table border="0" cellpadding="1" cellspacing="1" style="width:100%">
        <tbody>
                <tr>
                        <td>1</td>
                        <td>2</td>
                        <td>3</td>
                </tr>
                <tr>
                        <td>4</td>
                        <td>5</td>
                        <td>6</td>
                </tr>
        </tbody>
    </table>
    """,
    """
    <table border="0" cellpadding="1" cellspacing="1" style="width:100%">
        <tbody>
                <tr>
                        <td>1</td>
                        <td>2</td>
                        <td>3</td>
                </tr>
                <tr>
                        <td>4</td>
                        <td>5</td>
                        <td>6</td>
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
