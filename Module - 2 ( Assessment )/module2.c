#include<stdio.h>
#include<string.h>
char* reverse(char str1[], char str2[])
{
	int j,length,i;
	length = lengthOfString(str1);
	j=length-1;
	
	for(i=0; i<length;i++){
		str2[i]=str1[j];
		j--;
	}
	str2[length]='\0';
	
	return str2;
}

char* concatenation(char str1[],char str2[],char str3[])
{
	int l1,l2,i,j=0;
	
	l1=lengthOfString(str1);
	l2=lengthOfString(str2);
	
	for(i=0;i<l1; i++)
	{
		str3[i]=str1[i];
	}
	
	for(i=l1;i<l1+l2; i++)
	{
		str3[i]=str2[j++];
	}
	str3[l1+l2]='\0';
	return str3;
	
}

char* palindrome(char str1[],char str2[])
{
	int i,l,j;
	int flag=1;
	l=lengthOfString(str1);
	j=l-1;
	
	for(i=0;i<l;i++){
		str2[i]=str1[j];
		j--;
	}
	str2[l]='\0';
	for(i=0;i<l;i++){
		if(str1[i]!=str2[i]){
			flag=0;
		}
	}
	
	if(flag ==1){
		return "Palindrome";
	}
	else{
		return "Not Palindrome";
	}
}

char* copyAString(char str1[],char str2[])
{
	int i,l;
	l=lengthOfString(str1);
	
	for(i=0; i<l;i++){
		str2[i]=str1[i];
	}
	str2[l]='\0';
	return str2;
}

int lengthOfString(char str1[])
{
	int i,l;
	l=0;
	for(i=0; str1[i]!='\0'; i++){
		l++;
	}
	
	return l;
}

int frequency(char str1[], char f)
{
	int i,count=0;
	
	for(i=0; str1[i]!='\0'; i++){
		if(str1[i]==f){
			count++;
		}
	}
	
	return count;
}

void vowelAndConsonant(char str1[], char vowel[], char consonant[])
{
	int i,l,v,c,k,j,cvowel=0,cconsonant=0;
	l=lengthOfString(str1);
	v=lengthOfString(vowel);
	c=lengthOfString(consonant);
	
	for(i=0;i<l;i++){
		for(j=0; j<v; j++){
			if(str1[i]==vowel[j]){
				cvowel++;
			}
		}
		for(k=0; k<c; k++){
			if(str1[i]==consonant[k]){
				cconsonant++;
			}
		}
	}
	
	printf("\nVowels : %d",cvowel);
	printf("\nConsonant : %d",cconsonant);	
}
int blankAndSpace(char str1[])
{
	int i,space=0,digit=0;

	
	for(i=0;str1[i]!='\0';i++)
	{
		if(str1[i]== ' ')
		{
			space++;
		}
		else if((str1[i]=='0') || (str1[i]=='1') || (str1[i]=='2') || (str1[i]=='3') || (str1[i]=='4') || (str1[i]=='5') || (str1[i]=='6') || (str1[i]=='7') || (str1[i]=='8') || (str1[i]=='9'))
		{
			digit++;
		}
	}
	
	printf("\nBlank spaces: %d", space);
    printf("\nDigits: %d", digit);

}
void main()
{
	char str1[100],str2[100],choice,str3[200],f;
	char vowel[]="aeiouAEIOU";
	char consonant[]="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
	int option,i;
	do{
		printf("\n1-> Reverse a string : ");
		printf("\n2-> Concatenation : ");
		printf("\n3-> Palindrome : ");
		printf("\n4-> Copy a string : ");
		printf("\n5-> Length of the String : ");
		printf("\n6-> Frequency of character in string : ");
		printf("\n7-> Find the number of vowels and consonants : ");
		printf("\n8-> Find the number of spaces and digits : ");
		
		printf("\nEnter your option : ");
		scanf("%d",&option);
		
		getchar();
		
		switch(option)
		{
			case 1:
				printf("\nEnter the string : ");
				gets(str1);
				
				printf("\nReverse of string : %s",reverse(str1,str2));
				
			break;
			
			case 2:
				printf("\nEnter the 1st string : ");
				gets(str1);
				
				printf("\nEnter the 2nd string : ");
				gets(str2);
				
				printf("\nConcatenation of string  : %s",concatenation(str1,str2,str3));
				
			break;
			
			case 3:
				printf("\nEnter the 1st string : ");
				gets(str1);
				
				printf("\n%s",palindrome(str1, str2));
				
			break;
			
			case 4:
				printf("\nEnter the 1st string : ");
				gets(str1);
				
				printf("\nCopied string  : %s",copyAString(str1, str2));
				
			break;
			
			case 5:
				printf("\nEnter the 1st string : ");
				gets(str1);
				
				printf("\nLength of string  : %d",lengthOfString(str1));
				
			break;
			
			case 6:
				printf("\nEnter the 1st string : ");
				gets(str1);
				
				printf("\nEnter the character you want find (Frequency) : ");
				scanf(" %c",&f);
	
				printf("\nFrequency of %c : %d",f,frequency(str1,f));
				
			break;
			
			case 7:
				printf("\nEnter the string : ");
				gets(str1);
	
				vowelAndConsonant(str1,vowel,consonant);
				
			break;
			
			case 8:
				printf("\nEnter the string : ");
				gets(str1);
	
				blankAndSpace(str1);
				
			break;
			
			default:
				printf("\nPlease Enter valid choice!!!!!");
		}
		printf("\nDo you want to continue? (Y/y)Yes or (N/n)No : ");
		scanf(" %c",&choice);
	}
	while(choice=='Y' || choice=='y');
	
	printf("\n\n Program terminated successfully!!!!");
	
}
