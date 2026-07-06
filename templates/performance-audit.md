# Performance Audit Checklist

## Frontend

### Bundle Size
- [ ] Bundle total < 200KB gzip
- [ ] Code splitting por rota
- [ ] Lazy load de modulos nao-criticos
- [ ] Tree shaking habilitado
- [ ] Imagens otimizadas (WebP, AVIF, lazy load)
- [ ] Fontes com display: swap, subset

### Render Performance
- [ ] First Contentful Paint (FCP) < 1.8s
- [ ] Largest Contentful Paint (LCP) < 2.5s
- [ ] Time to Interactive (TTI) < 3.8s
- [ ] Total Blocking Time (TBT) < 200ms
- [ ] Cumulative Layout Shift (CLS) < 0.1

### Re-renders Desnecessarios
- [ ] React.memo / useMemo / useCallback onde apropriado
- [ ] Keys estaveis em listas
- [ ] Sem prop drilling excessivo
- [ ] Context splitado se necessario
- [ ] Virtualization em listas longas (> 100 items)

### Network
- [ ] HTTP/2 ou HTTP/3
- [ ] Cache-Control headers
- [ ] Compressao (gzip, brotli)
- [ ] CDN para assets estaticos
- [ ] Prefetch de rotas provaveis

## Backend

### Throughput
- [ ] Requests/segundo: capacidade medida
- [ ] P50, P95, P99 latency documentados
- [ ] Throughput em pico: capacidade medida
- [ ] Escala horizontal testada

### Database
- [ ] Queries < 100ms (P95)
- [ ] Indexes em colunas de busca
- [ ] N+1 queries eliminados
- [ ] Slow query log ativado
- [ ] Connection pool dimensionado
- [ ] Query cache onde apropriado

### Caching
- [ ] Redis/Memcached para dados quentes
- [ ] Cache invalidation strategy
- [ ] HTTP cache (ETag, Last-Modified)
- [ ] CDN para respostas cacheaveis
- [ ] Application-level cache para calculos caros

### Async
- [ ] Operacoes I/O async
- [ ] Filas para tarefas pesadas (Bull, Celery, SQS)
- [ ] WebSockets quando aplicavel
- [ ] Polling otimizado (long polling, SSE)

## Algoritmo

### Complexidade
- [ ] Big O analisado para funcoes criticas
- [ ] Sem loops O(n²) em datasets grandes
- [ ] Sem recursion profunda sem memoization
- [ ] Sorting/Binary Search quando apropriado

### Memoria
- [ ] Sem memory leaks (event listeners, timers)
- [ ] Streams para arquivos grandes (> 1MB)
- [ ] Paginated responses (nao carregar tudo)
- [ ] Object pooling para objetos pesados

## DevOps

### Monitoring
- [ ] APM (Application Performance Monitoring)
- [ ] Metricas em tempo real (Prometheus, Datadog)
- [ ] Alertas para SLO violado
- [ ] Distributed tracing

### Scaling
- [ ] Auto-scaling configurado
- [ ] Load balancer
- [ ] Health checks
- [ ] Graceful shutdown

## Output

```
PERFORMANCE AUDIT - [data]

METRICAS ATUAIS:
- LCP: X ms (meta: < 2500)
- TBT: Y ms (meta: < 200)
- Bundle: Z KB (meta: < 200)
- P95 latency: W ms (meta: < 500)

GARGALOS IDENTIFICADOS:
1. [local] - impacto
2. [local] - impacto

OTIMIZACOES PROPOSTAS (por ROI):
1. [mudanca] - ganho esperado: X - esforco: Y
2. [mudanca] - ganho esperado: X - esforco: Y

EXPECTATIVA APOS OTIMIZACOES:
- LCP: < 1500ms
- Bundle: < 150KB
- P95: < 300ms
```
