import random
import pygame
import sys

class Panel(object): 
    rect_arr=[] 
    moving_block=None 
    def __init__(self, bg, block_size, position):
        self._bg=bg
        self._x,self._y,self._width,self._height=position
        self._block_size=block_size
        self._bgcolor=[0,0,0]
    
    def add_block(self,block):
        for rect in block.get_rect_arr():
            self.rect_arr.append(rect)

    def change_block(self):
        if self.moving_block:
            new_arr = self.moving_block.change()
            if new_arr and not self.check_overlap(0, 0, check_arr=new_arr): 
                self.moving_block.rect_arr=new_arr

    def create_move_block(self):
        block = create_block()
        block.move(5-2,-2)  
        self.moving_block=block

    def check_overlap(self, diffx, diffy, check_arr=None):
        if check_arr is None: check_arr = self.moving_block.get_rect_arr()
        for x,y in check_arr:
            for rx,ry in self.rect_arr:
                if x+diffx==rx and y+diffy==ry:
                    return True
        return False

    def control_block(self, diffx, diffy):
        if self.moving_block.can_move(diffx,diffy) and not self.check_overlap(diffx, diffy):
            self.moving_block.move(diffx,diffy)

    def check_clear(self):
        pass

    def move_block(self):
        if self.moving_block is None: create_move_block()
        if self.moving_block.can_move(0,1) and not self.check_overlap(0,1): 
            self.moving_block.move(0,1)
        else:
            self.add_block(self.moving_block)
            self.check_clear()
            self.create_move_block()

    def paint(self):
        mid_x=self._x+self._width/2
        pygame.draw.line(self._bg,self._bgcolor,[mid_x,self._y],[mid_x,self._y+self._height],self._width) 
        
        # 绘制已经落底下的方块
        bz=self._block_size
        for rect in self.rect_arr:
            x,y=rect
            pygame.draw.line(self._bg,[0,0,255],[self._x+x*bz+bz/2,self._y+y*bz],[self._x+x*bz+bz/2,self._y+(y+1)*bz],bz)
            pygame.draw.rect(self._bg,[255,255,255],[self._x+x*bz,self._y+y*bz,bz+1,bz+1],1)
       
        # 绘制正在落下的方块
        if self.move_block:
            for rect in self.moving_block.get_rect_arr():
                x,y=rect
                pygame.draw.line(self._bg,[0,0,255],[self._x+x*bz+bz/2,self._y+y*bz],[self._x+x*bz+bz/2,self._y+(y+1)*bz],bz)
                pygame.draw.rect(self._bg,[255,255,255],[self._x+x*bz,self._y+y*bz,bz+1,bz+1],1)


class Block(object):
    sx=0
    sy=0
    def __init__(self):
        self.rect_arr=[]

    def get_rect_arr(self): 
        return self.rect_arr

    def move(self,xdiff,ydiff): 
        self.sx+=xdiff
        self.sy+=ydiff
        self.new_rect_arr=[]
        for x,y in self.rect_arr:
            self.new_rect_arr.append((x+xdiff,y+ydiff))
        self.rect_arr=self.new_rect_arr

    def can_move(self,xdiff,ydiff):
        for x,y in self.rect_arr:
            if y+ydiff>=20: return False
            if x+xdiff<0 or x+xdiff>=10: return False
        return True
    
    def change(self):
        self.shape_id+=1
        if self.shape_id >= self.shape_num:
            self.shape_id=0
        
        arr = self.get_shape()
        new_arr = []
        for x,y in arr:
            if x+self.sx<0 or self.sx>=10:
                self.shape_id -= 1
                if self.shape_id < 0:
                    self.shape_id = self.shape_num - 1
                return None

            new_arr.append([x+self.sx, y+self.sy])

        return new_arr


class LongBlock(Block):
    shape_id=0
    shape_num=2
    def __init__(self, n=None): 
        super(LongBlock, self).__init__()
        if n is None: n=random.randint(0,1)
        self.shape_id=n
        self.rect_arr=self.get_shape()

    def get_shape(self):
        if self.shape_id==0: return [(1,0),(1,1),(1,2),(1,3)] 
        else: return [(0,2),(1,2),(2,2),(3,2)]

class SquareBlock(Block): 
    shape_id=0
    shape_num=1
    def __init__(self, n=None):
        super(SquareBlock, self).__init__()
        self.rect_arr=[(1,1),(1,2),(2,1),(2,2)]

    def get_shape(self):
        return self.rect_arr

class ZBlock(Block): 
    shape_id=0
    shape_num=2
    def __init__(self, n=None):
        super(ZBlock, self).__init__()
        if n is None: n=random.randint(0,1)
        self.shape_id=n
        self.rect_arr=self.get_shape()
        
    def get_shape(self):
        if self.shape_id==0: 
            return [(2,0),(2,1),(1,1),(1,2)]
        else:
            return [(0,1),(1,1),(1,2),(2,2)]


class SBlock(Block): 
    shape_id=0
    shape_num=2
    def __init__(self, n=None):
        super(SBlock, self).__init__()
        if n is None: n=random.randint(0,1)
        self.shape_id=n
        self.rect_arr=self.get_shape()

    def get_shape(self):
        if self.shape_id==0:
            return [(1,0),(1,1),(2,1),(2,2)]  
        else:
            return [(0,2),(1,2),(1,1),(2,1)]

class LBlock(Block): 
    shape_id=0
    shape_num=4
    def __init__(self, n=None):
        super(LBlock, self).__init__()
        if n is None: n=random.randint(0,3)
        self.shape_id=n
        self.rect_arr=self.get_shape()

    def get_shape(self):
        if self.shape_id==0: return [(1,0),(1,1),(1,2),(2,2)]
        elif self.shape_id==1: return [(0,1),(1,1),(2,1),(0,2)]
        elif self.shape_id==2: return [(0,0),(1,0),(1,1),(1,2)]
        else: return [(0,1),(1,1),(2,1),(2,0)]

class JBlock(Block): 
    shape_id=0
    shape_num=4
    def __init__(self, n=None):
        super(JBlock, self).__init__()
        if n is None: n=random.randint(0,3)
        self.shape_id=n
        self.rect_arr=self.get_shape()

    def get_shape(self):
        if self.shape_id==0: return [(1,0),(1,1),(1,2),(0,2)]
        elif self.shape_id==1: return [(0,1),(1,1),(2,1),(0,0)]
        elif self.shape_id==2: return [(2,0),(1,0),(1,1),(1,2)]
        else: return [(0,1),(1,1),(2,1),(2,2)]

class TBlock(Block): 
    shape_id=0
    shape_num=4
    def __init__(self, n=None):
        super(TBlock, self).__init__()
        if n is None: n=random.randint(0,3)
        self.shape_id=n
        self.rect_arr=self.get_shape()

    def get_shape(self):
        if self.shape_id==0: return [(0,1),(1,1),(2,1),(1,2)]
        elif self.shape_id==1: return [(1,0),(1,1),(1,2),(0,1)]
        elif self.shape_id==2: return [(0,1),(1,1),(2,1),(1,0)]
        else: return [(1,0),(1,1),(1,2),(2,1)]
        

def create_block():
    n = random.randint(0,19)
    if n==0: return SquareBlock(n=0)
    elif n==1 or n==2: return LongBlock(n=n-1)
    elif n==3 or n==4: return ZBlock(n=n-3)
    elif n==5 or n==6: return SBlock(n=n-5)
    elif n>=7 and n<=10: return LBlock(n=n-7)
    elif n>=11 and n<=14: return JBlock(n=n-11)
    else: return TBlock(n=n-15)

if __name__ == '__main__':
    pygame.init()
    space=30
    main_block_size=30
    main_panel_width=main_block_size*10
    main_panel_height=main_block_size*20
    screencaption = pygame.display.set_caption('Tetris')
    screen = pygame.display.set_mode((main_panel_width+160+space*3,main_panel_height+space*2))
    main_panel=Panel(screen,main_block_size,[space,space,main_panel_width,main_panel_height])

    pygame.key.set_repeat(200, 30)
    main_panel.create_move_block()

    diff_ticks = 300 
    ticks = pygame.time.get_ticks() + diff_ticks

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
                 exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: main_panel.control_block(-1,0)
                if event.key == pygame.K_d: main_panel.control_block(1,0)
                if event.key == pygame.K_q: main_panel.change_block()
                if event.key == pygame.K_s: main_panel.control_block(0,1)
       
        screen.fill((100,100,100)) 
        main_panel.paint() 

        pygame.display.update() 

        if pygame.time.get_ticks() >= ticks:
            ticks+=diff_ticks
            main_panel.move_block()

