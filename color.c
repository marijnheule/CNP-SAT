#include <stdio.h>
#include <stdlib.h>

int main (int argc, char** argv) {
  FILE *graph;
  int colors, nVertex, nEdge, skip = -1;
  int *edges;

  graph  = fopen (argv[1], "r");
  colors = atoi  (argv[2]);
  if (argc > 3) skip = atoi (argv[3]) - 1;

  fscanf (graph, " p edge %i %i ", &nVertex, &nEdge);

  if (skip != -1) skip = skip % nVertex; 

  edges = (int*) malloc (sizeof(int) * 2*nEdge);

  int a, b;
  int size = 0;
  while (1) {
    int tmp = fscanf (graph, " e %i %i ", &a, &b);
    if (tmp == 0 || tmp == EOF) break;
    edges[size++] = a - 1;
    edges[size++] = b - 1; }


  printf ("p cnf %i %i\n", nVertex * colors, nVertex + nEdge * colors - (skip != -1));

  int i, j;
  for (i = 0; i < nVertex; i++) {
    if (i == skip) continue;
    for (j = 1; j <= colors; j++)
      printf ("%i ", i * colors + j);
    printf ("0\n"); }

  for (i = 0; i < nEdge; i++)
    for (j = 1; j <= colors; j++)
      printf ("-%i -%i 0\n", edges[2*i] * colors + j, edges[2*i + 1] * colors + j);
}
