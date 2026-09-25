# Interpretação não julga: perfil de risco e inconsistências vão para `validacao`

**Decidido:** `interpretacao` só registra o que o cliente disse. A classificação do perfil de risco e a detecção de inconsistências saem de lá e passam a ser de `validacao`. Totais (ex.: patrimônio total) são calculados por `financeiro`; quando o cliente declara um total, ele é registrado como declaração, para `validacao` conferir contra a soma dos itens.

**Alternativa considerada:** extrair `perfil_risco` (Conservador/Moderado/Arrojado) e marcar `alerta_inconsistencia` já na interpretação. Descartada: contradiz a regra de traduzir "cegamente" e põe julgamento num lugar que não pode perguntar ao cliente.

**Por quê:** consolidar declarações contraditórias exige escolher qual prevalece ou perguntar — e só `validacao` pergunta.
