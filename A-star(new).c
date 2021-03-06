#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#define N 6
int fringelist[N*N][3],f=0,best,e,MST[N],num=0;
void main()
{
	int cost[N][N]={{0,1,2,3,4,5},{1,0,2,3,4,5},{1,2,0,3,4,5},{1,2,3,0,4,5},{4,1,2,3,0,5},{5,1,2,3,4,0}};
	int start,i,j,gn=0,fn,pos,current,temp;
	int MST[N];
	for (i=0;i<N;i++)
	{
		MST[i]=-1; //initialising everything to a min value
	}
	for(e=0;e<N*N;e++)
	{
		fringelist[e][2]=INT_MAX;
	}
	printf("Enter the starting node");
	scanf("%d",&start);
	MST[num]=start;
	num+=1;
	current=prod_successor(MST,cost,start,start);
	printf("current=%d",current);
	MST[num]=current;
	num=num+1;
	//printf("**************************\n");
	while(num<N)
	{
		current=prod_successor(MST,cost,current,start);
		printf("\ncurrent=%d",current);
		MST[num]=current;
		num=num+1;
		//printf("**************************\n");
	}
	printf("\n");
	for (i=0;i<N;i++)
	{
		printf("%d->",MST[i]);
	}
	printf("%d",start);

}

int prod_successor(int MST[N], int cost[N][N], int current, int start)
{
	int res,i,j,gn,hn,min,pos=0;
	int flag=0;
	for (i=0;i<N;i++) //iterating through the cost matrix
	{
		flag=0;
		for (j=0;j<num;j++) //iterating through MST
		{
			if (i==MST[j])
			{
				flag=1; //present in MST, therefore do not include it
			}
		}
		if (flag==0)
		{
			//this particular column for the current node is NOT in the MST
			//safe to expand
			if (current!=i) //to avoid paths which are to the node itself
			{
				gn=cost[current][i];
				hn=est_dist_unvisited(cost,MST,num,i,start);
				fringelist[f][0]=current; //store the source
				fringelist[f][1]=i; //store the destination
				fringelist[f][2]=gn+hn; // storing fn
				f++;
			}
		}
	}
	//now the fringe list is ready... have a look at it and the least cos node to current, and return that node
	min=fringelist[0][2];
	for (i=1;i<f;i++)
	{
		if (fringelist[i][2]<=min)
		{
			min=fringelist[i][2];
			pos=i;
		}
	}
	/*for (i=0;i<k;i++)
	{
		printf("succ: %d -> %d\n", succ[i][0], succ[i][1]);
	}*/
	if (pos==current)
	{
		res=fringelist[pos][1];
	}
	else
	{
		//backtracking
		while(f>pos)
		{
			fringelist[f-1][2]=INT_MAX;
			for (i=0;i<num;i++)
			{
				if (fringelist[f-1][0]==MST[i])
				{
					MST[i]=-1;
					num--;
				}
			}
			f--;
		}
		MST[num]=fringelist[pos][0];
		num++;
		res=fringelist[pos][1];
	}
	return res; //node to be expanded
}

int est_dist_unvisited(int cost[N][N], int MST[N], int n, int current, int start) //n is the number of current elements in the MST
{
	int i=n,j,k,l,m,x=0,sum=0,flag=0,min,pos;
	int list[N][2];
	int MST_copy[N];
	for (m=0;m<N;m++)
	{
		MST_copy[m]=MST[m];
	}
	MST_copy[n]=current;
	n++;
	while(i<N-1) 																			//ATTENTION CHECKPOINT: added the = sign
	{
		x=0;
		for (j=0;j<N;j++)
		{
			flag=0;
			for (k=0;k<n;k++)
			{
				if (j==MST_copy[k])
				{
					flag=1; // that node is already present in the MST
				}
			}
			if (flag==1)
			{
				//do not include
			}
			else
			{
				if (current!=j)
				{
					list[x][0]=j;
					list[x][1]=cost[current][j];
					x++;
				}
			}
		}
		pos=0;
		min=list[pos][1];
		//printf("\nmin=%d",min);
		for (l=0;l<x;l++)
		{
			if (min>list[l][1])
			{
				min=list[l][1];
				pos=l;
			}
		}
		MST_copy[n]=list[pos][0];
		current=list[pos][0];
		n=n+1;
		sum+=min;
		i=i+1;
	}
	if (i==N-1)
	 {
		//last node remaining
		pos=MST_copy[n-1];
		sum+=cost[pos][current];
	}
	/*for (i=0;i<n;i++)
	{
		printf("%d,",MST_copy[i]);
	}*/
	//printf("\n");
	//printf("\nSum=%d",sum);
	return sum;
}
