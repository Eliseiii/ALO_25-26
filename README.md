# **Algebra Liniara si Optimizare**



---

## Tema 1 – Aritmetică flotantă și aproximarea funcției tangentă

### Exercițiul 1 – Precizia mașinii

Se determină cel mai mic număr pozitiv `u = 10⁻ᵐ` (`m ∈ ℕ`) pentru care calculatorul nu mai poate distinge `1.0 + u` de `1.0`:

```
1.0 +c u ≠ 1.0
```

Această valoare se numește **precizia mașinii** și ilustrează limitele reprezentării numerelor în virgulă mobilă.

---

### Exercițiul 2 – Non-asociativitatea operațiilor în virgulă mobilă

Se demonstrează că adunarea efectuată de calculator **nu este asociativă**. Folosind `x = 1.0`, `y = u/10`, `z = u/10` (unde `u` este precizia mașinii de la ex. 1):

```
(x +c y) +c z  ≠  x +c (y +c z)
```

Similar, se găsesc valori `x, y, z` pentru care și **înmulțirea** este non-asociativă:

```
(x ×c y) ×c z  ≠  x ×c (y ×c z)
```

---

### Exercițiul 3 – Aproximarea funcției tangentă prin polinoame

Se implementează o aproximare polinomială a funcției `tan(x)` bazată pe seria MacLaurin:

```
tan(x) ≈ x + (1/3)x³ + (2/15)x⁵ + (17/315)x⁷ + (62/2835)x⁹
```

**Cazuri tratate:**
- `x ∈ (-π/4, π/4)` – formula se aplică direct
- `x ∈ [π/4, π/2)` – se folosește relația `tan(x) = 1 / tan(π/2 - x)` pentru reducerea argumentului
- `x ∉ (-π/2, π/2)` – se aplică periodicitatea funcției și antisimetria `tan(x) = -tan(-x)`
- `x` multiplu de `π/2` – caz special, tratat separat (tangenta nedefinită)





---

## Tema 2 – Minimizarea funcțiilor de o variabilă prin metoda secantei

Se aproximează un punct de minim (local sau global) al unei funcții `F : ℝ → ℝ` folosind **metoda secantei** aplicată derivatei `F'(x) = 0`.

---

### Metoda secantei

Pornind de la două valori inițiale alese aleatoriu `x₀` și `x₁`, se construiește un șir convergent folosind relația de recurență:

```
x_{k+1} = x_k - Δx_k,    unde    Δx_k = (x_k - x_{k-1}) · g(x_k) / (g(x_k) - g(x_{k-1}))
```

unde `g(x) = F'(x)`. Algoritmul se oprește când `|Δx| < ε` sau când `|g(xₖ)| < ε`, cu un număr maxim de iterații `k_max = 1000`.

**Caz degenerat:** dacă `|g(xₖ) - g(xₖ₋₁)| ≤ ε`, numitorul este considerat nul și se setează `Δx = 10⁻⁵` (sau `Δx = 0` dacă `|g(x)| ≤ ε/100`, semn că s-a atins soluția).

---

### Aproximarea derivatelor

`F'(x)` se aproximează prin **două formule numerice** distincte, comparate între ele:

```
G1(x, h) = ( 3F(x) - 4F(x-h) + F(x-2h) ) / (2h)

G2(x, h) = ( -F(x+2h) + 8F(x+h) - 8F(x-h) + F(x-2h) ) / (12h)
```

`F''(x)` se aproximează cu formula:

```
F''(x) ≈ ( -F(x+2h) + 16F(x+h) - 30F(x) + 16F(x-h) - F(x-2h) ) / (12h²)
```

cu `h = 10⁻⁵` sau `10⁻⁶` (parametru de intrare).

---

### Ce face programul

1. **Găsește punctul critic** `x*` cu metoda secantei, folosind pe rând `G1` și `G2` pentru aproximarea lui `F'`
2. **Verifică dacă `x*` este punct de minim** prin condiția `F''(x*) > 0`
3. **Compară cele două formule** (`G1` vs `G2`) din punct de vedere al numărului de iterații necesare pentru aceeași precizie `ε`





---

## Tema 3 – Descompunere LU și rezolvarea sistemelor liniare

Această temă implementează algoritmul **Doolittle** de descompunere LU a unei matrice pătratice `A ∈ ℝⁿˣⁿ`, urmând rezolvarea unui sistem liniar `Ax = b` folosind metodele substituției directe și inverse.

### Ce face programul

1. **Descompunere LU** – se calculează (când este posibil) factorizarea `A = L·U`, unde:
   - `L` este matrice inferior triunghiulară cu `1` pe diagonală
   - `U` este matrice superior triunghiulară
   - Descompunerea se calculează **în-place**, direct în matricea `A`, fără alocare suplimentară

2. **Determinant** – se calculează `det(A) = det(L) · det(U)` eficient din elementele diagonalei lui `U`

3. **Rezolvarea sistemului `Ax = b`** – prin două etape:
   - **Substituție directă**: rezolvare `Ly = b`
   - **Substituție inversă**: rezolvare `Ux = y`

4. **Verificarea soluției** – se afișează norma euclidiană `‖A_init · x_LU − b_init‖₂`, care ar trebui să fie < `10⁻⁸`

5. **Comparare cu soluția din bibliotecă** – se calculează `x_lib` și `A⁻¹` folosind o bibliotecă standard și se afișează:
   - `‖x_LU − x_lib‖₂`
   - `‖x_LU − A⁻¹ · b_init‖₂`

### Restricții de implementare

- Se alocă **doar două matrice**: `A` (modificată pe parcurs) și `A_init` (copia datelor inițiale)
- Diagonala lui `L` (`lᵢᵢ = 1`) **nu se stochează** – este tratată explicit în algoritmul de substituție
- Verificarea diviziunii cu zero se face cu precizia `ε` (citită din input), nu cu comparație exactă: `|v| > ε`
- Programul trebuie să funcționeze corect pentru sisteme de dimensiuni **n > 100**

### Input

| Parametru | Descriere |
|-----------|-----------|
| `n` | Dimensiunea sistemului |
| `A` | Matricea sistemului (`n × n`) |
| `b` | Vectorul termenilor liberi (`n × 1`) |

---

## Tema 4 – Descompunere QR prin algoritmul Householder

Se implementează **algoritmul lui Householder** pentru factorizarea `A = Q·R` a unei matrice pătratice `A ∈ ℝⁿˣⁿ`, urmată de rezolvarea sistemului liniar `Ax = b` și calculul inversei matricei.

---

### Input

| Parametru | Descriere |
|---|---|
| `n` | Dimensiunea sistemului |
| `A` | Matricea pătratică (`n × n`) |
| `s` | Vector dat (`n × 1`), folosit pentru construirea lui `b` și verificarea soluției |

---

### Ce face programul

**1. Construirea vectorului `b`**

Vectorul termenilor liberi se calculează ca:
```
bᵢ = Σⱼ sⱼ · aᵢⱼ,    i = 1,...,n
```
Prin construcție, soluția exactă a sistemului `Ax = b` este chiar vectorul `s`.

---

**2. Descompunerea QR – Algoritmul Householder**

Se factorizează `A = Q·R` în `(n-1)` pași, folosind **matrice de reflexie** (Householder):
```
Pᵣ = Iₙ - (1/β) · u·uᵀ
```
La fiecare pas `r`, coloana `r` a matricei `A` este adusă în formă superior triunghiulară fără a modifica primele `(r-1)` coloane. Se actualizează simultan `A`, `b` și `Q̃ = Iₙ` (care acumulează `Qᵀ`).

La finalul algoritmului:
- `A` conține matricea `R` (superior triunghiulară)
- `Q̃` conține `Qᵀ`
- `b` conține `Qᵀ · b_init`

---

**3. Rezolvarea sistemului `Ax = b`**

Sistemul se reduce la un sistem superior triunghiular:
```
Ax = b  ⟺  Rx = Qᵀb
```
Se obțin două soluții comparate între ele:
- `x_Householder` – prin implementarea proprie
- `x_QR` – prin biblioteca standard

Se afișează: `‖x_QR - x_Householder‖₂`

---

**4. Verificarea erorilor**

Se calculează și afișează următoarele norme (toate ar trebui să fie < `10⁻⁶`):

| Normă | Descriere |
|---|---|
| `‖A_init · x_Householder - b_init‖₂` | Reziduul soluției Householder |
| `‖A_init · x_QR - b_init‖₂` | Reziduul soluției din bibliotecă |
| `‖x_Householder - s‖₂ / ‖s‖₂` | Eroarea relativă față de soluția exactă (Householder) |
| `‖x_QR - s‖₂ / ‖s‖₂` | Eroarea relativă față de soluția exactă (bibliotecă) |

---

**5. Calculul inversei `A⁻¹`**

Inversa se calculează rezolvând `n` sisteme liniare `Ax = eⱼ` (`j = 1,...,n`), unde `eⱼ` sunt vectorii bazei canonice. Pentru fiecare sistem:
1. Se inițializează `b = Qᵀ eⱼ` (coloana `j` din `Qᵀ`)
2. Se rezolvă `Rx = b` prin substituție inversă
3. Soluția `x*` devine coloana `j` a lui `A⁻¹_Householder`

Se compară cu inversa din bibliotecă și se afișează:
```
‖A⁻¹_Householder - A⁻¹_bibl‖₂
```

---

**6. Date random**

Programul suportă inițializare aleatorie a lui `A` și `s`, funcționând corect pentru orice dimensiune `n`.

---
