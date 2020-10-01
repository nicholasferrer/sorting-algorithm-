<h1>Comparação do tempo de execução dos três algoritmos implementados:</h1>

<h2> De acordo com os testes:
- Selection sort é o mais eficiente em vetores de 50, 500 e 5000 elementos.
- Bubble sort é o menos eficiente em vetores 50, 500 e 5000 elementos.
</h2>

<h1>Análise de Complexidade:</h1>
<h2>
<p>- Bubble sort: executa em O(n^2) independente de como o vetor estiver organizado</p>
<p>- Selection Sort: executa em O(n^2) independente de como o vetor estiver organizado -- realiza menos trocas</p>
<p>- Insertion Sort: executar em O(n) no melhor caso - quando o vetor está ordenado - e executa em O(n^2) no pior caso</p>
<p>Observação: o Bubble Sort pode ser melhorado para executar o melhor caso em O(n) quando o vetor estiver ordenado. Para isso, basta verificar se há troca no for interno; se não houver, é porque o vetor está ordenado. Assim, pode-se interromper a ordenação.</p>
</h2>