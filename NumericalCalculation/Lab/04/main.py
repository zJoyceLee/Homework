import copy

xuanjitu = '''
琴清流楚激弦商秦曲发声悲摧藏音和咏思惟空堂心忧增慕怀惨伤仁
房厢东步阶西游王姿淑窈窕伯召南周风兴自后妃荒经离所怀叹嗟智
兰休桃林阴翳桑怀归思广河女卫郑楚樊厉节中闱淫遐旷路伤中情怀
凋翔飞燕巢双鸠士迤逶路遐志咏歌长叹不能奋飞忘清帷房君无家德
茂流泉清水激扬思欣其人硕兴齐商双发歌我哀衣想华饰容朗镜明圣
熙长君思悲好仇旧蕤威璨翠荣曜流华观冶容为推感英曜珠光粉葩虞
阳愁叹发容摧伤乡悲情我感伤清徽宫羽同声相追所多思感堆为荣唐
春方殊离仁君荣身苦惟难生患多殷忧缠情将如何钦苍穹誓终笃志真
墙禽心滨均深身加怀幽是婴藻文繁虎龙宁自感思岑形萤城荣明庭妙
面伯改汉物日我兼思河漫漫荣曜华雕旌孜孜伤情幽未犹倾苟难闱显
殊在者之品润乎愁苦艰是丁丽壮观饰容侧君在时岩在炎在不受乱华
意域惑步育漫集悴我生何冤允颜曜绣衣梦想劳形峻慎盛戒义肤作重
感故匿风施衍殃少章时桑诗端无始始诗仁颜贞枣嵯深兴后姬原人容
故遗亲飘生思衍精崧盛翳风此平终璇情贤衰物岁峨虑渐孽班祸谗章
新旧间离天罪辜神恨昭感兴作苏心玑明别改知识深微至嬖女因佞臣
霜废远微地积何遐微业孟鹿丽氏诗国显行华终调渊察大赵婕所奸贤
冰故离隔德怨因幽玄倾宣鸣辞理兴义怨士容柏松重远伐氏妤诗凶为
齐君殊乔贵其备远悼思伤怀日往感年衰念是咎愆涯祸用飞辞恣害圣
洁子我本乎根旧旷叹永感悲思忧远劳情谁为独居经在昭燕辇极我配
志惟同堆均难苦离戚戚情哀暮岁殊叹时贱女怀叹网防丹实汉骄终英
清新衾阴匀寻辛风知我者谁世异浮奇倾鄙贱何如罗萌青生成盈贞皇
纯贞志一专所当麟沙流频游异浮沉华英翳曜潜阳林西昭景薄榆桑伦
望薇碎感通明神龙驰若然倏逝惟时年殊白日西移光滋愚谗浸顽凶匹
谁云浮寄身轻飞昭亏不盈无倏必盛有衰无日不陂流蒙谦退休孝慈离
思辉光饰璨殊文德离患体一违心意志殊愤激何施电疑危远家和雍飘
想群离散妾孤遗怀仪容仰俯荣华丽饬身将与谁为逝容节敦贞淑思浮
怀悲哀声殊乘分圣赀何情忧感惟哀忘节上通神只推持所贞记自恭江
所春伤应翔惟归皇辞成者作休下遗葑菲采者无差生从是敬孝为基湘
亲刚柔有女为贱人房忧处已悯薇身长路悲旷感士民梁山殊塞隔河津'''.strip()

xjt = xuanjitu.split('\n')


def poem_get(xjt, index):
    return xjt[index[0]][index[1]]

def print_poems_qiyan(xjt, poems):
    for poem in poems:
        for (idx,word_pos) in enumerate(poem):
            if idx % 7 == 0  and idx  != 0:
                print(', ', end='')
            print(poem_get(xjt, word_pos), end='')
        print()

def add1(i):
    return i+1

def dup(val, times):
    return [val for _ in range(times)]


(X,Y) = (0,1)
# Steps: (Up,Right,Down,Left)
(Up, Right, Down, Left) = (0, 1, 2, 3)

xjt_red = [
    [( -1,  7,  7, -1), ( -1,14,  7,  7), ( -1,  7,  7,14), ( -1, -1,  7,  7)],
    [(  7,  7,14, -1), (  7,14,  7,  7), (  7,  7,14,14), (  7, -1,14,  7)],
    [(14,  7,  7, -1), (14,14,  7,  7), (14,  7,  7,14), (14, -1,  7,  7)],
    [(  7,  7, -1, -1), (  7,14, -1,  7), (  7,  7, -1,14), (  7, -1, -1,  7)],
]
xjt_red_pos = [
    [(0,0), (0,7), (0,21), (0,28)],
    [(7,0), (7,7), (7,21), (7,28)],
    [(21,0), (21,7), (21,21), (21,28)],
    [(28,0), (28,7), (28,21), (28,28)],
]
xjt_black = (6,6)
xjt_blue = [(13,6), (6,13), (6,13), (13,6)]
xjt_yellow = (4,4)
xjt_magenta = [(5,4), (4,5), (4,5), (5,4)]
xjt_green = (5,5)
xjt_purple =  (3,3)

poems = []

# 自初行退一字，每首七言四句，俱逐句退成回文
def method1():
        poem = []
        poem = poem + \
               list(zip(
                   range(1, xjt_red[0][3][Down]-1),
                   dup(xjt_red_pos[0][3][Y], xjt_red[0][3][Down]-1)
               ))
        poems.append(poem)



class Path(object):

    def __init__(self, pos, matrix):
        self.pos = pos
        self.matrix = matrix
        self.matrix_row = len(matrix)
        self.matrix_col = len(matrix[0]) if (self.matrix_row > 0) else 0
        self.path =  []

    def __str__(self):
        return str(self.pos)

    def can_go(self, direction, path_num):
        if direction == Up:
            if self.pos[0] - (path_num - 1) < 0:
                return False
            return True
        elif direction == Right:
            if self.pos[1] + (path_num - 1) >= self.matrix_col:
                return False
            return True
        elif direction == Down:
            if self.pos[0] + (path_num - 1) >= self.matrix_row:
                return False
            return True
        elif direction ==  Left:
            if self.pos[1] - (path_num - 1) < 0:
                return False
            return True
        else:
            raise ValueError('Direction: ' + str(direction))
        return False

    def go(self, direction, path_num):
        if direction == Up:
            self.path = self.path + [(self.pos[0]-i, self.pos[1]) for  i in range(path_num)]
            self.pos[0] = self.pos[0] - path_num
        elif direction == Right:
            self.path = self.path + [(self.pos[0], self.pos[1]+i) for i in range(path_num)]
            self.pos[1] = self.pos[1] + path_num
        elif direction == Down:
            self.path = self.path +  [(self.pos[0]+i, self.pos[1]) for i in range(path_num)]
            self.pos[0] = self.pos[0] + path_num
        elif direction  == Left:
            self.path = self.path + [(self.pos[0], self.pos[1]-i) for i in range(path_num)]
            self.pos[1] = self.pos[1] - path_num
        else:
            raise ValueError('Direction: ' + str(direction))
        return self

    def get_path(self):
        return copy.deepcopy(self.path)


# Method 1: 自初行退一字，每首七言四句，俱逐句退成回文
def method1():
    ret = []
    for i in [Up,Right,Down,Left]:
        for j in [Up,Right,Down,Left]:
            for k in [Up,Right,Down,Left]:
                for l in [Up,Right,Down,Left]:
                    path = Path([1,28], xjt)
                    if path.can_go(i, 7):
                        path.go(i, 7)
                        if path.can_go(j, 7):
                            path.go(j, 7)
                            if path.can_go(k, 7):
                                path.go(k, 7)
                                if path.can_go(l, 7):
                                    path.go(l, 7)
                                    ret.append(path.get_path())
    return ret

# Method 2: 自上横行退一字成句，逐句逐字逆读，俱成回文
def method2():
    ret = []
    for i in [Up,Right,Down,Left]:
        for j in [Up,Right,Down,Left]:
            for k in [Up,Right,Down,Left]:
                for l in [Up,Right,Down,Left]:
                    path = Path([0,27], xjt)
                    if path.can_go(i, 7):
                        path.go(i, 7)
                        if path.can_go(j, 7):
                            path.go(j, 7)
                            if path.can_go(k, 7):
                                path.go(k, 7)
                                if path.can_go(l, 7):
                                    path.go(l, 7)
                                    ret.append(path.get_path())
    return ret

# print_poems_qiyan(xjt, [Path([1,28], xjt).go(Down,7).go(Down,14).go(Down, 7).get_path()])

poems += method1()
poems += method2()
print(len(poems))
print_poems_qiyan(xjt, poems)
