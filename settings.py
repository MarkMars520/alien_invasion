class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 背景的颜色

        self.ship_speed_factor = 1.5  # 飞船飞行的速度

        # 子弹设置
        self.bullet_speed_factor = 1  # 子弹飞行速度
        self.bullet_width = 3 #  3像素
        self.bullet_height = 15 # 15 像素高
        self.bullet_color = 60 , 60, 60
