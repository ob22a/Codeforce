# Codeforces Gym 102535/J - Aufbau Principle

[![Problem Link](https://img.shields.io/badge/Codeforces-102535/J-blue.svg)](https://codeforces.com/problemset/gymProblem/102535/J)

## Problem Description
You are a student of the Academy for Covert Missions, currently not doing your chemistry homework. Now, chemistry can be useful to secret agents in many ways – gunpowder, smoke bombs, poison – but you don't care about any of that. You want to be a Hacker Agent, the enigmatic guy in the hoodie watching various UI elements pop up on the screen, the guy spewing technical terms while rapidly hacking on the back of a speeding motorcycle. That's why you're going to make a computer program to do your homework for you!

An atom has one or more electron shells, and each shell itself has one or more subshells. The electrons of an atom are distributed across its different shells within the different subshells. The Aufbau Principle dictates how these electrons are distributed, which is called its electron configuration.

An example electron configuration is that of Oxygen (O), which is `1s² 2s² 2p⁴`. This means:

- in the first shell, there are 2 electrons in the zeroth subshell  
- in the second shell, there are 2 electrons in the zeroth subshell, and 4 electrons in the first subshell  

As in the example, the electron configuration of an element is represented by a series of terms of the form `nlᵉ`, where:

- `n` - a positive integer, representing the electron shell  
- `ℓ` - a non-negative integer, representing the "position" the subshell  
- `l` - a letter, which by convention we use instead of `ℓ` to depict the subshell  
- `e` - a positive integer, representing the number of electrons held by the shell  

The corresponding letters/labels for each subshell are:

| ℓ (number) | 0 | 1 | 2 | 3 |
|------------|---|---|---|---|
| l (letter) | s | p | d | f |

Each shell of an atom has a maximum number of subshells – in fact, the `n`th shell can have up to `n` subshells (thus, `0 ≤ ℓ < n`, always).

Each subshell of an atom has a maximum "capacity" – in other words, it can only fit a specific number of electrons. This capacity is determined solely by its `ℓ`, in particular: `2(2ℓ + 1)`. Thus:

- The `3p` subshell can fit `2(2·1 + 1) = 6` electrons  
- The `2p` subshell can also fit 6 electrons  
- The `4d` subshell can fit `2(2·2 + 1) = 10` electrons  

The Aufbau Principle states that the electrons of an atom fill up subshells (to their capacity) in order of increasing n+ℓ, and in ties, by increasing n , as illustrated in this diagram:

![Aufbau Principle Diagram](https://espresso.codeforces.com/8b31d759868dff0f8d289c46a8ff82ff56e2f39f.png)

For example:
- **Hydrogen** (1 electron): fills the zeroth subshell → `1s¹`  
- **Helium** (2 electrons): fills the zeroth subshell → `1s²`  
- **Lithium** (3 electrons): `1s² 2s¹`  
- **Potassium** (19 electrons): `1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹`  

Seeing this pattern, you figure out that you could make a simple program for this. You can even generalize it to the 10¹⁵th element! You hope that there are no exceptions to the Aufbau Principle. (Spoiler: there are, but you don't really care enough about chemistry to address them.)

For ℓ > 3, we use the following extended notation:

| ℓ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | ... |
|---|---|---|---|---|---|---|---|---|---|-----|
| l | s | p | d | f | g | h | i | j | k | ... |

Important notes:
1. 's' and 'p' are skipped in the extension
2. After 'z':
   - Two-letter combinations: aa, ab, ..., zz
   - Then three-letter: aaa, aab, ..., zzz
   - And so on...

The pattern continues as:
![Aufabu Principle Diagram 2](https://espresso.codeforces.com/a142d57d85df56a2de445f44c4c9c06c307173a5.png)

Now, given an atomic number (which is the same as its number of electrons), can you find the last electron shell, last subshell and number of electrons in the last shell in its electron configuration? In other words, what is the last "nle"? For example, if the given atomic number is 19, then the answer should be `4s¹`.

Output the answer as `n`, `l`, `e` in a single line NOT separated by spaces. For example, for 19, output `4s¹`.

**Input**  
The first line of input contains `t`, the number of test cases. `t` test cases follow.

Each test case is composed of a single line containing an integer `a` denoting an atomic number.

**Constraints**  
1 ≤ `t` ≤ 10⁵  
1 ≤ `a` ≤ 10¹⁵

**Output**  
For each test case, output a single line containing `n`, `l` and `e`, NOT separated by spaces. For example, for 19, output `4s¹`.

**Example**

**Input**
```
3
19
103
1000000000000000
```

**Output**
```
4s1
6d1
93591dzil31704
```