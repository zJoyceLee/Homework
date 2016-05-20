import MySQLdb
import random
import hashlib

try:
    db = MySQLdb.connect('localhost', 'root', '1', 'xk', charset='utf8')
    cursor = db.cursor()

    lastName = [
        '赵', '钱', '孙', '李', '周', '吴', '郑', '王',
        '冯', '陈', '楮', '卫', '蒋', '沈', '韩', '杨',
        '朱', '秦', '尤', '许', '何', '吕', '施', '张',
        '孔', '曹', '严', '华', '金', '魏', '陶', '姜',
        '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
        '云', '苏', '潘', '葛', '奚', '范', '彭', '郎',
        '鲁', '韦', '昌', '马', '苗', '凤', '花', '方',
        '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐',
        '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤',
        '滕', '殷', '罗', '毕', '郝', '邬', '安', '常'
    ]

    firstName = [
        '乐', '于', '时', '傅', '皮', '卞', '齐', '康',
        '伍', '余', '元', '卜', '顾', '孟', '平', '黄',
        '和', '穆', '萧', '尹', '姚', '邵', '湛', '汪',
        '祁', '毛', '禹', '狄', '米', '贝', '明', '臧',
        '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
        '熊', '纪', '舒', '屈', '项', '祝', '董', '梁',
        '杜', '阮', '蓝', '闽', '席', '季', '麻', '强',
        '贾', '路', '娄', '危', '江', '童', '颜', '郭',
        '梅', '盛', '林', '刁', '锺', '徐', '丘', '骆',
        '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍',
        '虞', '万', '支', '柯', '昝', '管', '卢', '莫',
        '经', '房', '裘', '缪', '干', '解', '应', '宗',
        '丁', '宣', '贲', '邓', '郁', '单', '杭', '洪',
        '包', '诸', '左', '石', '崔', '吉', '钮', '龚',
        '程', '嵇', '邢', '滑', '裴', '陆', '荣', '翁',
        '荀', '羊', '於', '惠', '甄', '麹', '家', '封',
        '芮', '羿', '储', '靳', '汲', '邴', '糜', '松',
        '井', '段', '富', '巫', '乌', '焦', '巴', '弓',
        '牧', '隗', '山', '谷', '车', '侯', '宓', '蓬',
        '全', '郗', '班', '仰', '秋', '仲', '伊', '宫',
        '宁', '仇', '栾', '暴', '甘', '斜', '厉', '戎',
        '祖', '武', '符', '刘', '景', '詹', '束', '龙',
        '叶', '幸', '司', '韶', '郜', '黎', '蓟', '薄'
    ]

    collegeName = [
        '通信与信息工程学院', '计算机工程与科学学院', '机电工程与自动化学院',
        '社区学院', '钱伟长学院', '理学院', '文学院', '外国语学院', '法学院',
        '材料科学与工程学院', '环境与化学工程学院'
    ]

    gender = ['Female', 'Male']

    ss = "INSERT INTO S(sno, sname, gender, age, sdept, pswd) VALUES "
    age = 22
    for year in ['12', '13', '14', '15']:
        for i in range(3000):
            student_id = year+'12'+'{0}'.format(i+1).zfill(4)
            name = random.choice(lastName)+random.choice(firstName)

            student_gender = random.choice(gender)

            college_name = random.choice(collegeName)

            passwd = student_id
            md5 = hashlib.md5()
            md5.update(passwd.encode())
            passwd_md5 = md5.hexdigest()

            sql = ss+"('{0}', '{1}', '{2}', {3}, '{4}', '{5}');".format(student_id, name, student_gender, age, college_name, passwd_md5)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        age = age - 1

    ss = "INSERT INTO T(tno, tname, tdept, pswd) VALUES "
    for i in range(100):
        teacher_id = '10001'+'{0}'.format(i+1).zfill(3)
        name = random.choice(lastName)+random.choice(firstName)
        college_name = random.choice(collegeName)

        passwd = teacher_id
        md5 = hashlib.md5()
        md5.update(passwd.encode())
        passwd_md5 = md5.hexdigest()

        sql = ss+"('{0}', '{1}', '{2}', '{3}');".format(teacher_id, name, college_name, passwd_md5)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    ss = "INSERT INTO C(cno, cname, credit, cdept, tno) VALUES "
    CES_className = [
        '面向对象程序设计', '离散数学', '数据结构', '计算机组成原理',
        '计算机网络', '操作系统', '电子技术',  '程序设计',
        '微机系统', '计算机系统结构', '编译原理',
         '数据库系统', '软件工程', '人工智能',
        '计算机图形学', '数字图像处理', '计算机通讯原理',
        '多媒体信息处理技术', '数字信号处理', '计算机控制',
        '网络计算', '算法设计与分析', '信息安全', '应用密码学基础',
        '信息对抗', '移动计算', '数论与有限域基础', '人机界面设计'
    ]

    tss = "SELECT tno FROM T WHERE tdept = '计算机工程与科学学院' ORDER BY 1;"
    cursor.execute(tss)
    CES_teacher = [i[0] for i in cursor.fetchall()]

    for i, name in enumerate(CES_className):
        course_id = '008305'+'{0}'.format(i+1).zfill(2)
        credit = random.randint(1, 5)
        tno = random.choice(CES_teacher)

        sql = ss+"('{0}', '{1}', {2}, '计算机工程与科学学院', '{3}');".format(course_id, name, credit, tno)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print(sql)
            db.rollback()

    tss = "SELECT tno FROM T WHERE tdept = '机电工程与自动化学院' ORDER BY 1;"
    cursor.execute(tss)
    EMSD_teacher = [i[0] for i in cursor.fetchall()]

    EMSD_className = [
        '电工技术', '电子技术', '机械设计基础', '机械加工机床',
        '机械加工工艺', '液压与气动技术', '检测技术', '数控技术',
        '电气控制技术', '单片机原理与应用',
        '可编程控制器及应用', '机电一体化系统与设计'
    ]
    for i, name in enumerate(EMSD_className):
        course_id = '008830'+'{0}'.format(i+1).zfill(2)
        credit = random.randint(1, 5)
        tno = random.choice(EMSD_teacher)
        sql = ss+"('{0}', '{1}', {2}, '机电工程与自动化学院', '{3}');".format(course_id, name, credit, tno)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    CIEI_className = [
        '通信工程', '电子技术', '电路分析', '通信电子线路',
        '脉冲数字电路', '数字信号处理', '信号与线性系统',
        '微机原理及应用', '电磁场理论', '微波技术与天线',
        '通信系统原理', '信息论与编码', '程控交换技术',
        '移动通信技术', '计算机网络通信', '光纤通信技术'
    ]
    tss = "SELECT tno FROM T WHERE tdept = '通信与信息工程学院' ORDER BY 1;"
    cursor.execute(tss)
    CIEI_teacher = [i[0] for i in cursor.fetchall()]
    for i, name in enumerate(CIEI_className):
        course_id = '008100'+'{0}'.format(i+1).zfill(2)
        credit = random.randint(1, 5)
        tno = random.choice(CIEI_teacher)
        sql = ss+"('{0}', '{1}', {2}, '通信与信息工程学院', '{3}');".format(course_id, name, credit, tno)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    other_className = [
        '电子商务导论', '中国传统思想文化','中西方哲学思想',
        '儒释道原典选读', '古代汉语', '中国哲学', '科学技术哲学',
        '民族与宗教漫谈', '实用收藏学', '逻辑基本原理', '西方政治思想',
        '台词表演', '教师礼仪与规范', '哲学与人生', '硬笔书法',
        '现代交际礼仪', '广告创意解析与大学生', '世界文化概论', '中国文化史',
        '美国文化', '汉语修辞与文化', '汉字与中国文化', '美学通论',
        '汉语方言趣谈', '世界文化遗产', '电工学B', '科技文献检索',
        '生物化学', '生物化学实验', '食品工程原理', '食品化学',
        '微生物学实验', '微生物学', '食品分析与实验', '食品安全与品质控制',
        '食品营养学', '食品加工原理', '食品机械与设备', '食品添加剂应用',
        '乳品工艺学'
    ]
    tss = """
    SELECT tno
    FROM T
    WHERE
        tdept != '通信与信息工程学院' and
        tdept != '机电工程与自动化学院' and
        tdept != '计算机工程与科学学院'
    ORDER BY 1;
    """
    cursor.execute(tss)
    other_teacher = [i[0] for i in cursor.fetchall()]
    for i, name in enumerate(other_className):
        course_id = '008000'+'{0}'.format(i+1).zfill(2)
        credit = random.randint(1, 5)
        tno = random.choice(other_teacher)
        sql = ss+"('{0}', '{1}', {2}, '{3}', '{4}');".format(course_id, name, credit, random.choice(collegeName[3:]), tno)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

finally:
    db.close()
