# **Algebra Liniara si Optimizare**


##Tema 1 -  Precizia maşină, neasociativitatea operațiilor elementare, aproximarea funcțiilor elementare

exercitiul 1 ✅
exercitiul 2 ✅
exercitiul 3 ✅

##Tema 2 - Minimizarea funcțiilor prin metoda secantei

Acest proiect este o aplicație de _optimizare numerică_ ce are scopul de a găsi automat punctul în care o funcție matematică $F(x)$ atinge cea mai mică valoare a sa.
HEAD
Procesul constă în aproximarea rădăcinii $x^*$ a ecuației neliniare $g(x)=0$ prin construcția unui șir de iterații $\{x_k\}$ care converge către soluția căutată

Procesul constă în aproximarea rădăcinii $x^*$ a ecuației neliniare $g(x)=0$ prin construcția unui șir de iterații $\{x_k\}$ care converge către soluția căutată


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
| `ε` | Precizia calculelor (ex: `10⁻⁶`) |
| `A` | Matricea sistemului (`n × n`) |
| `b` | Vectorul termenilor liberi (`n × 1`) |

---

Poți ajusta tonul sau adăuga secțiuni de **Usage** / **Example** dacă vrei să completez cu ceva specific (limbaj de programare, comenzi de rulare etc.).
