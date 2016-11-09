# Introdução

- Criado em 2007

- Primeira versão estável em 2009

- Dialeto de Lisp - "the programmable programming language"

- Linguagem de propósito geral com ênfase em programação funcional

- Compilado para Java Virtual Machine (JVM)

    - Com isso, é possível fazer chamar codigos Java pelo Closure e códigos Clojure em Java

- Pode ser compilado para JavaScript e ClojureCLR (tem uma ligação com o .NET)

- Linguagem compilada

- Hosted language: roda dentro da JVM e usa de funções como threading e garbage collection da JVM

---

# Clojure for the Brave and True

http://www.braveclojure.com/do-things/

---

# Programação Funcional:

* Não possui conceito de variáveis de estado, todo valor é único e imutável.

## Em Python:

* Listas: são dados dinâmicos (podem aumentar ou diminuir de tamanho) - Não segue o paradigma funciona!

* Tupla: são dados estáticos e imutáveis (não é possível adicionar, remover ou alterar elementos)

```
>>> a = (1, 2)
>>> print a[1]
2
>>> a[1] = 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError : 'tuple' object does not support item assignment
```

---

# First Things First: What Is Clojure?

> "Clojure was forged in a mythic volcano by Rich Hickey. Using an alloy of Lisp,
>  functional programming, and a lock of his own epic hair, he crafted a language that’s delightful yet powerful."


# Dependencias:
- Java

---

# Criando um novo projeto: Leiningen

> Leiningen - for automating Clojure projects without setting your hair on fire

- http://leiningen.org/

- Download the lein script (or on Windows lein.bat)

- Place it on your $PATH where your shell can find it (eg. ~/bin) - Aconselho a dar um echo $PATH e usar um daqueles

- Set it to be executable (chmod a+x ~/bin/lein)

- Run it (lein) and it will download the self-install package


## Creating the project:

```
lein new app <project_name>
```

## Estrutura criada

```
.
├── CHANGELOG.md
├── doc
│   └── intro.md
├── LICENSE
├── project.clj                # Equivalente ao setup.py
├── README.md
├── resources                  # Armazenar arquivos como imagens
├── src                        # Código fonte
│   └── dojo_example
│       └── core.clj
└── test                       # Testes
    └── dojo_example
        └── core_test.clj
```

---

# Entendendo o código criado

> src/dojo_example/core.clj

```
(ns dojo-example.core                      # ns: namespace
  (:gen-class))

(defn -main                                # defn: definindo função
  "I don't do a whole lot ... yet."
  [& args]
  (println "Hello, World!"))               # print

```

---

# Building

- Para criar um .jar, ou seja, ficar independente do lein, executar:

```
lein uberjar
```

- O arquivo gerado fica em:

```
.
├── target
│   └── uberjar
│       ├── classes
│       │   ├── dojo_example
│       │   │   ├── core.class
│       │   │   ├── core$fn__38.class
│       │   │   ├── core__init.class
│       │   │   ├── core$loading__5569__auto____36.class
│       │   │   └── core$_main.class
│       │   └── META-INF
│       │       └── maven
│       │           └── dojo-example
│       │               └── dojo-example
│       │                   └── pom.properties
│       ├── dojo-example-0.1.0-SNAPSHOT.jar
│       ├── dojo-example-0.1.0-SNAPSHOT-standalone.jar       <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Standalone
│       └── stale
│           └── leiningen.core.classpath.extract-native-dependencies
```

# Rodando

```
java -jar target/uberjar/clojure-noob-0.1.0-SNAPSHOT-standalone.jar
```

---

# Modo iterativo (REPL)

> Read-Eval-Print Loop

Equivalente à rodar o interpretador ```python```

```
lein repl
```

## Alguns exemplos

```
dojo-example.core=> (+ 1 2 3 4)
10
dojo-example.core=> (* 1 2 3 4)
24
dojo-example.core=> (first [1 2 3 4])
1

(do (println "Start") (println (+ 1 3)) (println "End"))
```

---

# Syntax

> Sério, estamos acabando essa parte

## Sintaxe básica

### Comentário
```
; Isso é um comentário de linha que é totalmente ignorado
(comment "Isso é um comentário, porém ele tem que ser uma expressão válida [isso é uma string]")
(comment Esse também é um comentário, porém o interpretador ainda passa por aqui, e isso pode gerar erro [aqui ele considera tudo string ainda])
(comment a : b) ; Inválido

```

### Tipos básicos
```
1                                         ; number
"batata"                                  ; string
[1 2 3 "abc"]                             ; vector
{:1 "abc"}                                ; maps
```

### Operações
```
(operator operand1 operand2 ... operandn) ; operation
```
- Vantagem: toda as operações tem mesma estrutura, independente do operador ou do tipo de dado.

---

### Fluxo de controle
- 'if'
```
; (if <bool> <eval-true> <eval-false>)
(if true "The true output" "The false output")
(if true (if false "The true true" "The true false") "The false output")
(if false "Empty second value") ; nil expected
```
> Diference de Python, valores como 0 e [] são considerados 'true'. 'nil' é considerado 'false'
> Para fazer mais de uma operação em algum caso, usar 'do'


- 'do'
```
; (do <first_thing> <second_thing> .... <return_value>
(println (do (println "First thing") (println "Second thing") "Return thing"))
```

- 'when'
> Combina 'if' e 'do' e sempre retorna 'nil' se for 'false'
```
;(when <first_thing> <second_thing> .... <return_value>)
(when <bool> (println "aaa") (println "bbb") (println "ccc") "Was true")
```

- Comparar tipo de retorno
```
;(type? <target>)
(true? true)
(string? "abc")
```

- Comparar valores
```
;(= <target_1> <target_2>)
(= 1 nil)
```

- 'and'
> Retorna primeiro valor 'false' ou o último valor
```
;(and <target_1> ... <target_n>)
(and true true false)
```


- 'or'
 > Retorna primeiro valor 'true' ou o útlimo valor
```
;(or <target_1> ... <target_n>)
(or false nil :large_I_mean_venti :why_cant_I_just_say_large)
```

---

- definindo variáveis
```
;(def variable-name <what-you-want>)
(def best_variable 13)
```

- 'map'
```
{:first-name "Charlie" :last-name "McFishwich"}
(hash-map :first-name "Charlie" :last-name "McFishwich")
```
Obs: (map ...) não cria um 'map', é feito para mapear vetores. Exemplo: ```(map inc [0 1 2 3])```

> Acessando valores com 'get'
```
;(get <map> <pos> [<return if empty>])
([get] {:a 0 :b 1} :c "unicorns?") ; get pode ser omitido!
```

- 'keywords'
:<expected_kw>
```
(:d {:a 1 :b 2 :c 3} "No gnome knows homes like Noah knows") ;Example
```

- 'list' x 'vector'
- Lista
> Lista não pode ser acessada com 'get', é preciso usar nth
```
'(1 2 3 4)
(nth '(:a :b :c) 0)
(list 1 "two" {3 4})
(conj '(1 2 3) 4)
```
>  Usar lista quando for adicionar elementos no começo da sequencia ou estiver escrevendo uma macro.
> Caso contrário, usar vetor.

- 'sets'
```
#{"kurt vonnegut" 20 :icicle}
(hash-set 1 1 2 2)
(conj #{:a :b} :b)
(set [3 3 3 4 4])
```

- 'contains'
```
(contains? #{:a :b} :a)
```


---

# Simplicidade
Clojure tem ênfase em simplicidade, encorajando a usar estruturas built-in ao invés de classes.

> It is better to have 100 functions operate on one data structure than 10 functions on 10 data structures.
> —Alan Perlis

---

# Funções
> ((or + -) 1 2 3)

- Recursão
```
(+ (inc 199) (/ 100 (- 7 2)))
(+ 200 (/ 100 (- 7 2))) ; evaluated "(inc 199)"
(+ 200 (/ 100 5)) ; evaluated (- 7 2)
(+ 200 20) ; evaluated (/ 100 5)
220 ; final evaluation
```


- Definindo uma função
```
;(defn <function_name>
;  <doctstring (OPTIONAL)>
;  [<parameters>]
;  <body>)

(defn example
  "This is a example function"
  [best_variable_ever]
  (do (println best_variable_ever) (println "End of function") "batata")
)
```

-Multi argumentos
```
(defn many-args
  ([]
    (many-args "I had no args, but I want have some")) ; recursão!
  ([first]
    (str "One arg: " first))
  ([first second]
    (str "Two args: " first second))
)
```

- "python args"
Usar & no argumento para concatenar todos os argumentos a mais em uma lista
```
(use '[clojure.string :only (join split)])

(defn trying
  ([name_1 name_2 & other_names]
    (str "I like " name_1 ". I like " name_2 ". " (when other_names (str "But I don't know " (join "and" other_names))))
  )
)
```

- Destructuring
Dar nome a posições dentro de uma coleção

```
(defn destructuwhat
  [[first-elem second-elem & others]]
  (println first-elem second-elem "and the others: " others)
)

(destructuwhat ["a" "b" "c" "d"])
```


- Function Body





---
REPL



The Forest of Tooling - A friendly and efficient programming environment makes it easy to try your ideas. You’ll learn how to set up your environment.
The Mountain of Language - As you ascend, you’ll gain knowledge of Clojure’s syntax, semantics, and data structures. You’ll learn how to use one of the mightiest programming tools, the macro, and learn how to simplify your life with Clojure’s concurrency constructs.
The Cave of Artifacts - In its depths you’ll learn to build, run, and distribute your own programs, and how to use code libraries. You’ll also learn Clojure’s relationship to the Java Virtual Machine ( JVM).
The Cloud Castle of Mindset - In its rarefied air, you’ll come to know the why and how of Lisp and functional programming. You’ll learn about the philosophy of simplicity that permeates Clojure, and how to solve problems like a Clojurist.
