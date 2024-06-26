﻿board=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.5]
youLost=Label('',200,200,size=75,fill='white',border='black',bold=True)
youLost2=Label('',200,275,size=75,fill='white',border='black',bold=True)
message=Group(Rect(0,170,400,120,fill='white'),Label('Use mouse, W.A.S.D or arrow keys.'  ,200,185,size=25),Label('Same number squares merge,',200,215,size=25),Label(' and try to get to the highest number.',200,245,size=25),Label('Use escape to save and tab to load.',200,275,size=25))
squareGroup=Group()
zeros=[]
app.stepsPerSecond=0.5
app.keySquareNum=0
def check():
    action=False
    app.keySquareNum=0
    for i in range(15):
        if board[app.keySquareNum+1]==0 and not board[app.keySquareNum]==0:
            if not (app.keySquareNum+1==4 or app.keySquareNum+1==8 or app.keySquareNum+1==12 or app.keySquareNum+1==16):
                action=True
        app.keySquareNum+=1
    app.keySquareNum=15
    for i in range(16):
        if not board[app.keySquareNum]==0:
            if board[app.keySquareNum+1]==board[app.keySquareNum] and not (app.keySquareNum==3 or app.keySquareNum==7 or app.keySquareNum==11 or app.keySquareNum==15):
               action=True
        app.keySquareNum-=1
    app.keySquareNum=15
    for i in range(16):
        if board[app.keySquareNum-1]==0 and not board[app.keySquareNum]==0:
            if not app.keySquareNum-1==-1:
                if not (app.keySquareNum-1==3 or app.keySquareNum-1==7 or app.keySquareNum-1==11):
                    action=True
        app.keySquareNum-=1
    app.keySquareNum=0
    for i in range(16):
        if not app.keySquareNum==0 and not board[app.keySquareNum]==0 :
            if board[app.keySquareNum-1]==board[app.keySquareNum] and not (app.keySquareNum==0 or app.keySquareNum==4 or app.keySquareNum==8 or app.keySquareNum==12):
               action=True
        app.keySquareNum+=1
    app.keySquareNum=0
    for i in range(12):
        if not board[app.keySquareNum]==0:
            if board[app.keySquareNum+4]==0 and not app.keySquareNum==12:
                action=True
        app.keySquareNum+=1
    app.keySquareNum=11
    for i in range(12):
        if not board[app.keySquareNum]==0:
            if board[app.keySquareNum]==board[app.keySquareNum+4]:
                action=True
        app.keySquareNum-=1
    app.keySquareNum=15
    for i in range(12):
        if not board[app.keySquareNum]==0:
            if board[app.keySquareNum-4]==0:
                action=True
        app.keySquareNum-=1
    app.keySquareNum=11
    for i in range(12):
        if not board[app.keySquareNum]==0:
            if board[app.keySquareNum]==board[app.keySquareNum+4]:
                action=True
        app.keySquareNum-=1
    return(action)


pickColor={
    0:'gray',
    2:'red',
    4:'orange',
    8:'yellow',
    16:'green',
    32:'blue',
    64:'darkviolet',
    128:'pink',
    256:rgb(255, 195, 30),
    512:rgb(255, 255, 100),
    1024:'lightgreen',
    2048:'cornflowerBlue',
    4096:'mediumSlateBlue',
    8192:'darkred',
    16384:'darkorange',
    32768:'gold',
    65536:'darkgreen',
    131072:'white',
    262144:'purple',
}




def score():
    app.keySquareNum=0
    e=0
    for i in range(16):
        e+=board[app.keySquareNum]
        app.keySquareNum+=1
    return(e)
def drawBoard():
    squareGroup.clear()
    squareNum=0
    topY=0
    sideX=0
    for i in range(16):
        b='black'
        t='black'
        if board[squareNum]==2.1:
            board[squareNum]=2
            b='white'
        elif board[squareNum]==4.1:
            board[squareNum]=4
            b='white'
        elif board[squareNum]==131072:
            t='black'
        squareGroup.add(Rect(sideX,topY,100,100,fill=pickColor[board[squareNum]],border=b))
        if not board[squareNum]==0:
            squareGroup.add(Label(board[squareNum],sideX+50,topY+50,size=150/len(str(board[squareNum])),bold = True,fill=t))
        sideX+=100
        if sideX==400:
            sideX=0
            topY+=100
        squareNum+=1
    if score()>=262140:
        youLost.value='You Win!'
        youLost.toFront()
    elif not check():
        youLost.value='You Lost!'
        youLost2.value=score()
        youLost.toFront()
        youLost2.toFront()
for i in range(2):
    app.keySquareNum=0
    for i in range(16):
        if board[app.keySquareNum] ==0:
            zeros.append(app.keySquareNum)
        app.keySquareNum+=1
    board[choice(zeros)]=2
drawBoard()
message.toFront()
def onKeyPress(key):
    message.visible=False
    action=False
    if key=='d':
        onKeyPress('right')
    elif key=='a':
        onKeyPress('left')
    elif key=='s':
        onKeyPress('down')
    elif key=='w':
        onKeyPress('up')
    elif 'right' in key:
        for i in range(4):
            app.keySquareNum=0
            for i in range(15):
                if board[app.keySquareNum+1]==0 and not board[app.keySquareNum]==0:
                    if not (app.keySquareNum+1==4 or app.keySquareNum+1==8 or app.keySquareNum+1==12 or app.keySquareNum+1==16):
                        board[app.keySquareNum+1]=board[app.keySquareNum]
                        board[app.keySquareNum]=0
                        action=True
                app.keySquareNum+=1
        app.keySquareNum=15
        for i in range(16):
            if not board[app.keySquareNum]==0:
                if board[app.keySquareNum+1]==board[app.keySquareNum] and not (app.keySquareNum==3 or app.keySquareNum==7 or app.keySquareNum==11 or app.keySquareNum==15):
                   board[app.keySquareNum+1]=board[app.keySquareNum]*2
                   board[app.keySquareNum]=0
                   action=True
            app.keySquareNum-=1
        for i in range(4):
            app.keySquareNum=0
            for i in range(15):
                if board[app.keySquareNum+1]==0 and not board[app.keySquareNum]==0:
                    if not (app.keySquareNum+1==4 or app.keySquareNum+1==8 or app.keySquareNum+1==12 or app.keySquareNum+1==16):
                        board[app.keySquareNum+1]=board[app.keySquareNum]
                        board[app.keySquareNum]=0
                        action=True
                app.keySquareNum+=1
    elif 'left' in key:
        for i in range(4):
            app.keySquareNum=15
            for i in range(16):
                if board[app.keySquareNum-1]==0 and not board[app.keySquareNum]==0:
                    if not app.keySquareNum-1==-1:
                        if not (app.keySquareNum-1==3 or app.keySquareNum-1==7 or app.keySquareNum-1==11):
                            board[app.keySquareNum-1]=board[app.keySquareNum]
                            board[app.keySquareNum]=0
                            action=True
                app.keySquareNum-=1
        app.keySquareNum=0
        for i in range(16):
            if not app.keySquareNum==0 and not board[app.keySquareNum]==0 :
                if board[app.keySquareNum-1]==board[app.keySquareNum] and not (app.keySquareNum==0 or app.keySquareNum==4 or app.keySquareNum==8 or app.keySquareNum==12):
                   board[app.keySquareNum-1]=board[app.keySquareNum]*2
                   board[app.keySquareNum]=0
                   action=True
            app.keySquareNum+=1
        for i in range(4):
            app.keySquareNum=15
            for i in range(16):
                if board[app.keySquareNum-1]==0 and not board[app.keySquareNum]==0:
                    if not app.keySquareNum-1==-1:
                        if not(app.keySquareNum-1==3 or app.keySquareNum-1==7 or app.keySquareNum-1==11):
                            board[app.keySquareNum-1]=board[app.keySquareNum]
                            board[app.keySquareNum]=0
                            action=True
                app.keySquareNum-=1
    elif 'down' in key:
        for i in range(4):
            app.keySquareNum=0
            for i in range(12):
                if not board[app.keySquareNum]==0:
                    if board[app.keySquareNum+4]==0 and not app.keySquareNum==12:
                        board[app.keySquareNum+4]=board[app.keySquareNum]
                        board[app.keySquareNum]=0
                        action=True
                app.keySquareNum+=1
        app.keySquareNum=11
        for i in range(12):
            if not board[app.keySquareNum]==0:
                if board[app.keySquareNum]==board[app.keySquareNum+4]:
                    board[app.keySquareNum+4]=board[app.keySquareNum]*2
                    board[app.keySquareNum]=0
                    action=True
            app.keySquareNum-=1
        for i in range(4):
            app.keySquareNum=0
            for i in range(12):
                if not board[app.keySquareNum]==0:
                    if board[app.keySquareNum+4]==0 and not app.keySquareNum==12:
                        board[app.keySquareNum+4]=board[app.keySquareNum]
                        board[app.keySquareNum]=0
                        action=True
                app.keySquareNum+=1
    elif 'up' in key:
        for i in range(4):
            app.keySquareNum=15
            for i in range(12):
                if not board[app.keySquareNum]==0:
                    if board[app.keySquareNum-4]==0:
                        board[app.keySquareNum-4]=board[app.keySquareNum]
                        board[app.keySquareNum]=0
                        action=True
                app.keySquareNum-=1
        app.keySquareNum=11
        for i in range(12):
            if not board[app.keySquareNum]==0:
                if board[app.keySquareNum]==board[app.keySquareNum+4]:
                    board[app.keySquareNum+4]=board[app.keySquareNum]*2
                    board[app.keySquareNum]=0
                    action=True
            app.keySquareNum-=1
        for i in range(4):
            app.keySquareNum=15
            for i in range(12):
                if not board[app.keySquareNum]==0:
                    if board[app.keySquareNum-4]==0:
                        board[app.keySquareNum-4]=board[app.keySquareNum]
                        board[app.keySquareNum]=0
                        action=True
                app.keySquareNum-=1
    if 'up' or 'down' or 'left' or 'right' in key:
        zeros.clear()
        app.keySquareNum=0
        for i in range(16):
            if board[app.keySquareNum] ==0:
                zeros.append(app.keySquareNum)
            app.keySquareNum+=1
        if not len(zeros)==0 and action:
            board[choice(zeros)]=choice([2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,4.1])
            drawBoard()
    if key=='escape':
        app.keySquareNum=0
        save=''
        for i in range(16):
            save= save + str(board[app.keySquareNum]**3)+' '
            app.keySquareNum+=1
        app.getTextInput('copy the text betwen the quotes "'+save+'  "then press ok.')
    elif key=='tab':
        inport(app.getTextInput('pase in the save and pess ok.'))
        pass
app.oldX=0
app.oldY=0
def onMousePress(x,y):
    app.oldX=x
    app.oldY=y
    message.visible=False
def onMouseRelease(x,y):
    z=angleTo(app.oldX,app.oldY,x,y)
    print(str(app.oldX)+','+str(app.oldY)+','+str(z))
    if distance(app.oldX,app.oldY,x,y)>50:
        if z >315 or z < 45:
            onKeyPress('up')
        elif z >45 and  z < 135:
            onKeyPress('right')
        elif z >135 and  z < 225:
            onKeyPress('down')
        elif z >225 and  z < 315:
            onKeyPress('left')
    app.oldx=0
    app.oldY=0
def inport(text):
    app.keySquareNum=0
    charNum=0
    piece=''
    for i in range(len(text)+1):
        if not str(text)[charNum:charNum+1]==' ':
            piece=piece+text[charNum:charNum+1]
        else:
            board[app.keySquareNum]=rounded(int(piece)**(1/3))
            piece=''
            app.keySquareNum+=1
        charNum+=1
    drawBoard()