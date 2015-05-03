% Parthesh Bulbule
% Indian Institute of Space Science and Technology 
% Mtech in Geoinformatics
% Subject: Spatial Data Modelling and Analysis
% Assignment-2



%% Program to plot voronoi diagram of given points


clc;
clear all;
close all;


%% Initialisation
Pts=[15 95;20 30;25 50;30 75;22 8;40 22;52 48;58 95;68 68;75 35;70 15;88 90];   %sites
N=size(Pts,1);
combos = combntns(1:12,3);
TR=triangulation(combos,Pts);
C=circumcenter(TR);    % Circumcentres of all possible triangles from the sites
X=C;
lc=size(C,1);



for ii=1:lc
    a=1;
    for jj=1:N
        if(combos(ii,1)~=jj && combos(ii,2)~=jj && combos(ii,3)~=jj && a==1)
            d1=sum((C(ii,:)-Pts(combos(ii,1),:)).^2);    %radius of circumcircle
            d2 = sum((C(ii,:)-Pts(jj,:)).^2);
            if d2<d1
                a=0;
                X(ii,:)=[0 0];
            end
        end
    end
end

j=1;
for ii=1:lc
    
    if(X(ii,1)~=0)
        Y(j,:)=X(ii,:);
        j=j+1;
    end
end


tri=find(X(:,1)~=0);
lim=size(tri,1);


plot(Pts(:,1),Pts(:,2),'bo','MarkerSize',10);
title('VORONOI DIAGRAM');
axis equal;
hold on
plot(Y(:,1),Y(:,2),'rx','MarkerSize',10);


for ii=1:lim
    a=combos(tri(ii),:);
    for jj=1:lim
        if (jj~=ii)
            
            d11= sum((Y(jj,:)-Pts(a(1),:)).^2);
            d22= sum((Y(jj,:)-Pts(a(2),:)).^2);
            d33= sum((Y(jj,:)-Pts(a(3),:)).^2);
            
                if (abs(d11-d22)<1 || abs(d11-d33)<1 || abs(d22-d33)<1)
                    line([Y(ii,1),Y(jj,1)],[Y(ii,2),Y(jj,2)],'LineWidth',2,'LineStyle','-','Color',[0 1 0]);
                end
            
                           
        end
            
    end
end

legend('Sample Points','Voronoi polygon vertices','Voronoi polygon edge','Location','northoutside','Orientation','horizontal');

