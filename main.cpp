#include <iostream>

using namespace std;
char a[3][3];
int main()
{
    int m=0,n=0;
    char k='1';
    ///filling the array
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
        {
            a[j][i]=k;
            k++;
        }
    }
//table design
    for(int i=0; i<7; i++)
    {
        if(i%2==0)
        {
            for(int j=0; j<7; j++)
            {

                cout<<"* ";

            }
        }
        else
            for(int j=0; j<7; j++)
            {
                if(j%2==0)
                {
                    cout<<"* ";
                }
                else
                {
                    cout<<a[n][m]<<" ";
                    if(n==2)
                    {
                        m++;
                        n=0;

                    }
                    else
                    {
                        n++;
                    }
                }
            }
        cout<<endl;
    }
    //Game state
    for(int i=0; i<9; i++)
    {
        char s;
        int row,col;
        //player 1
        if(i%2==0)
        {
            int x;
            cout<<"X turn"<<endl;
            cin>>x;
            s='X';
            if(x>6)
            {
                row=2;
                col=x-7;
            }
            else if(x>3)
            {
                row=1;
                col=x-4;
            }
            else
            {
                row=0;
                col=x-1;
            }
            a[col][row]='X';
        }
        //player 2
        else
        {
            int x;
            cout<<"O turn"<<endl;
            cin>>x;
            s='O';
            if(x>6)
            {
                row=2;
                col=x-7;
            }
            else if(x>3)
            {
                row=1;
                col=x-4;
            }
            else
            {
                row=0;
                col=x-1;
            }
            a[col][row]='O';

        }

        //table state
        m=0;
        n=0;
        for(int p=0; p<7; p++)
        {
            if(p%2==0)
            {
                for(int o=0; o<7; o++)
                {
                    if(o%2==0)
                    {


                        cout<<"* ";
                    }
                    else
                        cout<<"* ";
                }
            }
            else
                for(int o=0; o<7; o++)
                {
                    if(o%2==0)
                    {
                        cout<<"* ";
                    }
                    else
                    {
                        cout<<a[n][m]<<" ";
                        if(n==2)
                        {
                            m++;
                            n=0;

                        }
                        else
                        {
                            n++;
                        }
                    }
                }
            cout<<endl;
        }
//checking for a winner
        for(int r1=0; r1<3; r1++)
        {
            for(int h1=0; h1<3; h1++)
            {
                if(a[h1][r1]!=s)

                    break;

                else if(a[h1][r1]==s&&h1==2)
                {
                    cout<<s<<" WINS";
                    return 0;
                }
            }
        }
        for(int h1=0; h1<3; h1++)
        {
            for(int r1=0; r1<3; r1++)
            {
                if(a[h1][r1]!=s)
                    break;

                else if(a[h1][r1]==s&&r1==2)
                {
                    cout<<s<<" WINS";
                    return 0;
                }
            }
        }


        if(a[0][0]==s&&a[1][1]==s&&a[2][2]==s)
        {
            cout<<s<<"WINS"<<endl;
            return 0;
        }
        else if(a[0][2]==s&&a[1][1]==s&&a[2][0]==s)
        {
            cout<<s<<"WINS"<<endl;
            return 0;
        }
    }
    cout<<"DRAW";
    return 0;
}
