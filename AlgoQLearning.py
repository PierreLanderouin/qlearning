
'''
Maze est une matice (tableau à deux dimension) qui représente le labyrinthe, Ici chaque case de la matrice contient une liste qui :
En indice 0 contient un string qui est soit "but" si c'est la case but soit "pas bus" si c'est une autre case
En indice 1 un dico qui contient les différentes directions associés à leur poids
'''

listeChemin = [] #ListeChemin contient le chemin que parcourera le robot de sa case de depart à sa 
#case d'arriver

'''
Voici la fonction Q
dans le laby
'''



def Qlearning():
              
              
    listeChemin.append(position)
 
    '''
    Si la case courante où se trouve le robot est la case but
    '''
   
    if(maze[dest[0]][dest[1]][0]=="but"): 
   
        '''
        On attribut à la case précédente parcourue par le robot le poid de 
        100 à l'arc que le robot a pris, cet arc est en fait la direction d 
        qui a été choisi pour arriver à la case courant
        '''
    
        maze[listeChemin[len(listeChemin)-2][0]][listeChemin[len(listeChemin)][1]][d]=100
        
        '''
        on vide le chemin et on revient sur la case de départ
        '''
        listeChemin=[]
        
        position[0]=0
        position[1]=0
        
        '''
        d prend une direction aléatoire
        '''
        
        d=moves[random.randint(0,len(moves)-1)]
        
        '''
        Sinon si on  est pas sur la case but mais que l'on est sur une autre
        case
        '''
        
    else:
        
        
        
        '''
        on regarde les 4 arcs et on determine le poid max de l'ensemble 
        des arcs 
        
        '''
        
        tampon=0 
        
        for arc in maze[position[0]][position[1]][1]: #On parcours chaque arc et on regarde celui qui a le plus fort poid
            
        
            
            poid = maze[position[0]][position[1][1][arc]


            
	    if poid>tampon:
                tampon=poid
       
                
        """
        le tampon contient le poid max parmi les 4 arc (Par exemple si Gauche=8, Droite=9 et Haut=13 le tampon prend la valeur de 13)
         
        """
         
        """
        la valeur attribué
        à l'arc précédent qui a été parcouru sera tampon-1
        """
        
        """
        Si le tampon est plus grand que 0 dans ce cas la le robot va prendre la
        direction qui a le plus fort poid soit le poid égal au tampon
        """
      
	
        
        if(tampon>0):
        
        """
        On va ensuite attribuer la valeur tampon-1 à l'arc qui vient d'être
        parcourue
        """
        
            matrice[listeChemin[len(listeChemin-2)][0]][listeChemin[len(listeChemin-2)][1]][d]=tampon-1
            
            for arc in maze[position[0]][position[1]][1]:
                if(maze[position[0]][position[1]][1][arc]==tampon):
                    d=arc
                    
                    """
                    il faut mainteant prendre la direction de l'arc qui a le 
                    poid tampon (poid max)
                    """
                    
        else:
            
            """
            Si le tampon vaut O (c'est à dire que tous les arcs valent 0) le robot
            se déplace aléatoirement
            """
            d=moves[random.randint(0,len(moves)-1)]
            
        
