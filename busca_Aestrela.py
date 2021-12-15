
#@Autor : Yuri Domingos
# Data : 25 - 11 - 2021
# Objectivo : Resolver a busca clássica " A* - Estrela )
# Integrantes do grupo
# 21400 – Denizia Fernanda Cassombe Cazequene
# 20973 – Edson Paulo Augusto Gregório
# 21711 – Yuri Francisco António Domingos


arvore = {

    'A' : [['C',14], ['B',8]],
    'B' : [['D',38]],
    'C' : [['B',9],['D',24],['E',7]],
    'D' : [['G',9]],
    'E' : [['F',9], ['G',29], ['D',13]],
    
}

heuristica = { 'A': 30, 'B' : 26, 'C' : 21, 'D' : 7, 'E':22, 'F': 36,'G':0 } 
custo = { 'A' : 0}   # Total do custo para cada node visitado  

def busca_A_Estrela():

    global arvore, heuristica

    

    fechado = []
    aberto = [['A',30]]

    verdade = True


    ''' Encontrando os nodes visitados ou seja os elementos que estao na estrutura closed  ''' 

    while verdade :
    
        fn = [i[1] for i in aberto]  # com esta linha acedemos o segundo valor da nossa estrutura e usamos como limite do for 

        index_escolhido = fn.index(min(fn))  # encontra o menor valor do array aberto, 
        node = aberto[index_escolhido][0]    # Apresenta o caractere deste deste menor elemento encontrado 
        fechado.append(aberto[index_escolhido])

        del aberto[index_escolhido]  # Eliminamos a primeira instancia 
        
        if fechado[-1][0] == 'G':
            break

        for item  in arvore[node] :

            if item[0] in [ item_fechado[0] for item_fechado in fechado] :  # verificamos se nosso primeiro elemento esta na lista ou n nao
                continue

            custo.update( {item[0] : custo[node] + item[1]})  # se nao estiver actulizamos o dicionario adicionamos com o custo real 
            fn_node = custo[node]+ heuristica[item[0]]+item[1]  # Nesta linha pegamos o node actual com o seu valor real e adicionamos a heuristica ( f(n) = g(n) + h(h))

            temp = [item[0], fn_node]
            aberto.append(temp)   # O loop continua e assim vamos adicionando todos elementos da nossa lista 

    ''' Encontrando o melhor caminho  ''' 

    trace_node = 'G'  # Nosso nó objectivo 
    sequencia_optima = ['G']

    for i in range(len(fechado)-2,-1,-1):

        verificar_node = fechado[i][0]

        if trace_node in [custo_filho[0] for custo_filho in arvore[verificar_node]]:

            custo_filho = [temp[1] for temp in arvore[verificar_node]]
            node_filho  = [temp[0] for temp in arvore[verificar_node]]

            if custo[verificar_node] + custo_filho[node_filho.index(trace_node)] == custo[trace_node]:
                sequencia_optima.append(verificar_node)
                
                trace_node = verificar_node
    
    sequencia_optima.reverse()
    return fechado, sequencia_optima

if __name__ == '__main__':

    nodes_visitados, node_eficientes = busca_A_Estrela()
    print("No visitados " + str(nodes_visitados))
    print("Sequencia dos nos eficientes " + str(node_eficientes))
  
  
