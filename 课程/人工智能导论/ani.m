function animal()
%animal.m 动物识别专家系统
H=feature(); %输入需要进行识别动物的特征信息
%clc;

[A,flag]=distinguish(H); %正向推理输入信息
explain(A,flag); %对推理给出必要的解释
return;

function y=feature()
%inputdata.m 建立知识库，要求用户输入数据%
H=zeros(20,1); %知识库，存放系统求解问题所需要的知识，T为动物特征信息的数组
disp('All the questions 1 present yes，0 present no，else present ignoring this question');
q=input('1. if the animal has hair?    ');
if q==1
   H(1)=1; 
end
q=input('2. if the animal produce milk?    ');
if q==1
    H(2)=1;
end
q=input('3. if the animal has feather?    ');
if q==1
    H(3)=1;
end
q=input('4. if the animal flies?    ');
if q==1
    H(4)=1;
end
q=input('5. if the animal produce eggs?    ');
if q==1
    H(5)=1;
end
q=input('6. if the animal feeds on meat?    ');
if q==1
    H(6)=1;
end
q=input('7. if the animal has sharp teeth?    ');
if q==1
    H(7)=1;
end
q=input('8. if the animal has claws?    ');
if q==1
    H(8)=1;
end
q=input('9. if the animal stare at the front?    ');
if q==1
    H(9)=1;
end
q=input('10. if the animal has hoofs?    ');
if q==1
    H(10)=1;
end
q=input('11. if the animal ruminates?    ');
if q==1
    H(11)=1;
end
q=input('12. if the animal is brownish yellow?    ');
if q==1
    H(12)=1;
end
q=input('13. if the animal has dark spots?    ');
if q==1
    H(13)=1;
end
q=input('14. if the animal has dark bands?    ');
if q==1
    H(14)=1;
end
q=input('15. if the animal has long neck?    ');
if q==1
    H(15)=1;
end

q=input('16. the animal is black or white?    ');
if q==1
    H(17)=1;
end
q=input('17.if the animal can swim?    ');
if q==1
    H(18)=1;
end
y=H;
return;
 
function [A,flag]=distinguish(H)
%distinguish.m 规则库、推理机的建立%
%H 为动物名称的数组，flag 为记录规则是否被激发的数组
M=zeros(4,1); %存放中间推理结果，哺乳动物、食肉动物、有蹄类哺乳动物、鸟
A=zeros(7,1); %存放推理结果，豹、虎、长颈鹿、斑马、鸵鸟、企鹅、信天翁
flag=zeros(15,1); %进行状态标记，记录被激发的规则
temp=1; %用于判断规则库中是否有新的规则激发，大于0表示有新规则激发
while temp>0
    temp=0;
    if ~flag(1)&&H(1) %规则1
        M(1)=1;
        flag(1)=1;
        temp=temp+1;
    end
    if ~flag(2)&&H(2) %规则2
        M(1)=1;
        flag(2)=1;
        temp=temp+1;
    end  
    if ~flag(3)&&H(3) %规则3
        M(4)=1;
        flag(3)=1;
        temp=temp+1;
    end    
    if ~flag(4)&&H(4)&&H(5) %规则4
        M(4)=1;
        flag(4)=1;
        temp=temp+1;
    end
    if ~flag(5)&&H(6) %规则5
        M(2)=1;
        flag(5)=1;
        temp=temp+1;
    end  
    if ~flag(6)&&H(7)&&H(8)&&H(9) %规则6
        M(2)=1;
        flag(6)=1;
        temp=temp+1;
    end
    if ~flag(7)&&M(1)&&H(10) %规则7
        M(3)=1;
        flag(7)=1;
        temp=temp+1;       
    end
    if ~flag(8)&&M(1)&&H(11) %规则8
        M(3)=1;
        flag(8)=1;
        temp=temp+1;
    end
    if ~flag(9)&&M(1)&&M(2)&&H(12)&&H(13) %规则9
        A(1)=1;
        flag(9)=1;
        temp=temp+1;
    end
    if ~flag(10)&&M(1)&&M(2)&&H(12)&&H(14)&&H(18) %规则10
        A(2)=1;
        flag(10)=1;
        temp=temp+1;
    end
    if ~flag(11)&&M(3)&&H(15)&&H(13) %规则11
        A(3)=1;
        flag(11)=1;
        temp=temp+1;
    end
    if ~flag(12)&&M(3)&&H(14) %规则12
        A(4)=1;
        flag(12)=1;
        temp=temp+1;
    end
    if ~flag(13)&&M(4)&&H(15)&&H(17) %规则13
        A(5)=1;
        flag(13)=1;
        temp=temp+1;
    end
    if ~flag(14)&&M(4)&&H(18)&&H(17) %规则14
        A(6)=1;
        flag(14)=1;
        temp=temp+1;
    end
    if ~flag(15)&&M(4)&&H(4) %规则15
        A(7)=1;
        flag(15)=1;
        temp=temp+1;
    end    
end
return;
 
function explain(A,flag)
%explain.m 解释部分，负责对推理进行必要的解释%
%flag(i)=1,表示第i条规则被激发
if sum(A)~=1
    disp('ES cannot distinguish the animal，not in database');
    return;
end
 
if flag(1)==1 
     disp('because the animal has hair,it is a mammal');
end
if flag(2)==1
     disp('because the animal produce milk,it is a mammal');
end
if flag(3)==1
     disp('because the animal has feather,it is a bird');     
end
if flag(4)==1
     disp('because the animal can fly and produce eggs,it is a bird');  
end
if flag(5)==1
     disp('because the animal eat meat,it is a predator'); 
end
if flag(6)==1
     disp('because the animal have sharp teeth and have craws and stares at the front,it is a predator'); 
end     
if flag(7)==1
     disp('because the animal is a mammal and has hoofs,it is a mammal with hoofs');  
end    
if flag(8)==1
     disp('because the animal is a mammal and ruminates,it is a mammal with hoofs');  
end      
if flag(9)==1
     disp('because the animal is a mammal and a predator and is brownish yellow and has dark spots,it is a leopard');  
end   
if flag(10)==1
     disp('because the animal is a mammal and a predator and is brownish yellow and has dark bands,it is a tiger');  
end    
if flag(11)==1
     disp('because the animal is a mammal with hoofs and has long neck and has dark spots,it is a giraffe');  
end 
if flag(12)==1
     disp('because the animal is a mammal with hoofs and black bands,it is a zebra');  
end   
if flag(13)==1
     disp('because the animal is a bird and cannot fly and has long neck and has long legs and is dark-white,it is a ostrich');  
end 
if flag(14)==1
     disp('because the animal is a bird and cannot fly and can swim and is dark-white,it is a penguin');  
end 
if flag(15)==1
     disp('because the animal is a bird and can fly,it is a albatross');  
end   
return;