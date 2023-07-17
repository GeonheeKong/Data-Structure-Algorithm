str='''내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다.
내가 그의 이름을 불러주었을 때, 그는 내게로 와 꽃이 되었다.
내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞는 누가 나의 이름을 불러다오.
그에게로 가서 나도 그의 꽃이 되고 싶다.
우리들은 모두 무엇이 되고 싶다.
나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다'''

a=[]
b=[]
c=[]
e=[]
if __name__=="__main__":
    for i in str:
        if 'ㄱ'<=i and '힣'>=i:
            a.append(i)
            
            if i not in b:
                b.append(i)
    

        
    for i in range(0,len(b)):
        c.append(a.count(b[i]))
        
    
    for i in range(0,len(b)):
        d=(b[i],c[i])
        e.append(d)

    

    for i in range(0,len(e)):
            
    
    
    



        
     

