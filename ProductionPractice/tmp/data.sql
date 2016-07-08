INSERT INTO User(username, password, phone, email, addr) VALUES(
'lishu', '61949d4433dbc266a84dab7e04dafe77', '15618130000', 'testShoppingSystem@yeah.net', '上海市宝山区上大路99号上海大学'
);

INSERT INTO User(username, password, phone, email, addr) VALUES(
'liuziying', 'c43c413f14e020eceed4040fb37bad12', '18717810000', 'testShoppingSystem@yeah.net', '上海市宝山区上大路99号上海大学'
);

INSERT INTO User(username, password, phone, email, addr) VALUES(
'liyuzhe', 'f0bcf4d1b7ec7a162d6a6d402f5a5c6f', '18717890000', 'testShoppingSystem@yeah.net', '上海市宝山区上大路99号上海大学'
);

INSERT INTO Commodity(id, name, price, info) VALUES (
'ILCE7SM2', 'Sony/索尼 ILCE-7SM2 A7SM2 A7S2 微单 全画幅 相机 感光利器 五轴防抖 4K内录 最高ISO 409600', 24179, '
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
'
);

INSERT INTO Commodity(id, name, price, info) VALUES (
'ILCE7A72', 'Sony/索尼 ILCE-7(FE24-240mm) A7 全画幅微单套装 一镜走天下', 11598, '
<table border="0" cellpadding="1" cellspacing="1" style="width:100%">
    <tbody>
            <tr>
                    <td>品牌: Sony/索尼</td>
                    <td>像素: 约 2430万</td>
                    <td>有效像素传感器尺寸: 约 35.8x23.9mm</td>
            </tr>
    </tbody>
</table>
'
);

INSERT INTO Commodity(id, name, price, info) VALUES (
'ILCE7A71', 'Sony/索尼 ILCE-7 A7 全画幅微单相机 2430万 像素 混合 自动对焦', 12979, '
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
'
);

INSERT INTO Image(commodity_id, img_path) VALUES (
'ILCE7SM2', 'SonyILCE-7SM2A7SM2A7S2_1 .jpg');

INSERT INTO Image(commodity_id, img_path) VALUES (
'ILCE7SM2', 'SonyILCE-7SM2A7SM2A7S2_2 .png');

INSERT INTO Image(commodity_id, img_path) VALUES (
'ILCE7SM2', 'SonyILCE-7SM2A7SM2A7S2_3 .png');

INSERT INTO Image(commodity_id, img_path) VALUES (
'ILCE7A72', 'SonyLCE-7(FE24-240mm)A7_1.jpg');

INSERT INTO Image(commodity_id, img_path) VALUES (
'ILCE7A72', 'SonyLCE-7(FE24-240mm)A7_2.png');

INSERT INTO Image(commodity_id, img_path) VALUES (
'ILCE7A72', 'SonyLCE-7(FE24-240mm)A7_3.png');
INSERT INTO Image(commodity_id, img_path) VALUES (
'ILCE7A71', 'SonyLCE-7(FE24-240mm)A7_1.jpg');

INSERT INTO Image(commodity_id, img_path) VALUES (
'ILCE7A71', 'SonyLCE-7(FE24-240mm)A7_2.png');

INSERT INTO Image(commodity_id, img_path) VALUES (
'ILCE7A71', 'SonyLCE-7(FE24-240mm)A7_3.png');
