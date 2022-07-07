#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
#No início, o programa mostrará a seguinte lista de operações:




while True:

        print("Escolha uma das operações:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        op=int(input("Digite sua operação:"))

        if(op<0 and op>4):
            continue

        elif(op==0):
            break
            
        n1=int(input("digite um valor"))
        n2=int(input("digite um valor"))

        if(op==1):
                {
                     print("resultado =",n1+n2)
                }
        elif(op==2):
                    {
                        print("resultado =",n1-n2)
                    }

        elif(op==3):
                    {
                        print("resultado =",n1*n2)
                    }

        elif(op==4):
                    {
                        print("resultado =",n1/n2)
                    }   
                                

        else:
                {
                    print("Essa opção não existe")
                }
