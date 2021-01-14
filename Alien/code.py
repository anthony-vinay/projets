while True :
    import os
    x = input("Bonjour, veuillez rentrez votre numéro de carte sociale : ")

    #déboggage
    #print (len(x))
    #print (x[])
    #Code de sécurité sociale ex : B76797AIQQQ81X001W651W732X761ZZZZZZZZZZZZZZZZ

    if len(x) != 45 : # S'assurer que le code fait bien 45 caractères de long
        raise Exception ("La taille de votre code doit être exactement de 45 caractères")

    else :

        #Rendre en majuscule le code de sécurité sociale
        code = x.upper()

        #Initialisation
        os.system ("echo Informations sur le detenteur de la carte : " + code + " > informations.txt")

        # On cherche à connaître le sexe.
        def sexe (i,y) :
            if code[i] == "F"  :
                os.system ("echo Sexe " + y + "  : Foo >> informations.txt")
            elif code[i] == "B" :
                os.system ("echo Sexe " + y + " : Bar >> informations.txt")

            elif code[i] == "Q" :
                os.system ("echo Sexe " + y + " : Qux >> informations.txt")

            elif code[i] == "N" :
                os.system ("echo Sexe " + y + " : Norf >> informations.txt")

            elif code[i] == "X" :
                os.system ("echo Sexe " + y + " : Xiq >> informations.txt")

            elif code[i] == "W" :
                os.system ("echo Sexe " + y + " : Wuf >> informations.txt")

        #Si le sexe n'est pas existant (pour les martiens xD)
            else :
                raise Exception ("Sexe invalide, nous ne pouvons donner réponse à votre demande. Veuillez réessayer. ")
        sexe(0,"detenteur")

        #Déterminer l'année de naissance et s'assurer que ce dernier est un entier
        def annee (a,b,qui) :
            x = int(code[a:b])
            if isinstance (x, int) :
                os.system ("echo Annee de naissance " + qui + " : " + code [a:b] + " >> informations.txt ")

        try :
            annee (1,4,"detenteur")

        # Si l'année de naissance n'est pas un entier
        except ValueError :
            print ("Votre année de naissance doit être un entier.")

        #Année Martienne
        def annee_mars () :
            pass # Pas d'idée

        #Déterminer le secteur de naissance.
        try :
            x = int(code[4:6])
            if isinstance (x, int) and x >=0 and x < 97 :
                os.system ("echo Secteur de naissance : " + code [4:6] + " >> informations.txt ")
            elif isinstance (x, int) and x == 97 :
                os.system ("echo Secteur de naissance : Hors Mars >> informations.txt ")
            else :
                raise Exception ("Veuillez donner un secteur plausible entre 00 et 96 ou 97 si vous ne venez pas de Mars.")

        # Si le secteur de naissance n'est pas un entier
        except ValueError :
            print ("Votre secteur de naissance doit être un entier.")

        #Prénom
        x = code [6:11]
        consonnes = ["B","C","D","F","G","H","J","K","L","M","N","P","R","S","T","V","W","X","Z"]
        z = x.count("Q") #Savoir si le prénom fait moins de 5 lignes

        for i in range (len(consonnes)) :
            conforme = x.count(consonnes[i]) #L'intégralité du prénom sera comparé à chaque lettre présente dans la liste ci-dessus.
            if conforme == 1 :
                raise Exception ("Il existe ce prénom ?!? Pas chez les martiens apparemment... ")
            else :
                pass

        os.system("echo Prenom : " + code [6:11-z] + " >> informations.txt ")

        #Tentacules
        try :
            x = int(code[11:12])
            if isinstance (x, int) and x >= 2 :
                os.system ("echo Nombre de Tentacules : " + code [11:12] +  " >> informations.txt ")
        except ValueError :
            print ("Un nombre de tentacules réaliste s'il vous plait")

        #Antennes
        try :
            x = int(code[12:13])
            if isinstance (x, int) and x>=0 and x <=2 :
                os.system ("echo Nombre d'antennes : " + code [12:13] +  " >> informations.txt ")
        except ValueError :
            print ("Un nombre d'antennes réaliste s'il vous plait")

    #--Parenté---#

    #Fonction parent
        def peuvent_etre_parent () :
            Z = code[13].count("W") # Sexe 1er parent
            X = code[17].count("W") # Sexe 2eme parent
            Y = code[21].count("W") # Sexe 3eme parent

            if code[1:3] <= code[14:17] or code [1:3] <= code[18:21] or code [1:3] <= code[22:25] :
                raise Exception ("Parenté impossible")
            else :
                if Z + X + Y >= 2  : # Si deux parents ou plus (3) sont de sexe Wuf
                    pass
                else  :
                    if Z  == 1 and code[17] == code[21] : #Si 1er parent est Wuf
                        raise Exception ("Parenté impossible")

                    elif X == 1 and code[13] == code[21] : #Si 2eme parent est Wuf
                        raise Exception ("Parenté impossible")

                    elif Y == 1 and code[13]==code[17] : #Si 3eme parent est Wuf
                        raise Exception ("Parenté impossible")

                    elif code[13]==code[17] or code[17] == code[21] or code[13] == code[21] : # Si aucun parent n'est Wuf
                        raise Exception ("Parenté impossible")

        #1er parent
        sexe(13,"parent 1")
        annee(14,17,"parent 1")

        #2eme parent
        sexe(17,"parent 2")
        annee(18,21,"parent 2")

        #3eme parent
        sexe(21,"parent 3")
        annee(22,25,"parent 3")

        peuvent_etre_parent()

    #---Situation amoureuse---#

        #Fonction marriage
        def marriage (y) :
            w = (25 + 4 * y) - 4 #Code du détenteur avant marriage
            x = (25 + 4 * y) # début code époux(se)
            nvxcode = code [0:25] + code [w:x]
            os.system ("echo Voici le code de mariage numéro >> informations.txt " + str(y) + ": " + nvxcode + "ZZZZ"*4 )

        #Fonction divorce
        def divorce () :
            pass # Pas d'idée

        #Célibat
        if code[25:29] == "ZZZZ" :
            os.system ("echo Celibataire >> informations.txt")
        else :
            #1er époux
            sexe(25,"epoux 1")
            annee(26,29,"epoux 1")
            marriage(1)

            if code[29:33] == "ZZZZ" : #2nd époux
                os.system ("echo Sans autre epoux >> informations.txt")
            else :
                sexe(29,"epoux 2")
                annee(30,33,"epoux 2")
                marriage(2)

                if code [33:37] == "ZZZZ" : #3eme époux
                    os.system ("echo Sans autre epoux >> informations.txt")

                else :
                    sexe(33,"epoux 3")
                    annee(34,37,"epoux 3")
                    marriage(3)

                    if code[37:41] == "ZZZZ": #4eme époux
                        os.system ("echo Sans autre epoux >> informations.txt")

                    else :
                        sexe(37,"epoux 4")
                        annee(38,41,"epoux 4")
                        marriage(4)

                        if code[41:45] == "ZZZZ" :  #5eme époux
                            os.system ("echo Sans autre epoux >> informations.txt")
                        else :
                            sexe(41,"epoux 5")
                            annee(42,45,"epoux 5")
                            marriage(5)


        #Afficher le contenu
        fichier = open("informations.txt", "r")
        ligne = fichier.readline()
        while ligne:
            print(ligne)
            ligne = fichier.readline()
        fichier.close()
