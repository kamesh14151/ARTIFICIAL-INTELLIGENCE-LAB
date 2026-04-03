#  Family Facts & Queries in Prolog

## Aim
To implement and solve **AI-based problems** using **SWI-Prolog**, demonstrating the principles of **logic programming**.

---

## Algorithm

1. **Define parent/2 fact**  
   - Represents family relationships.

2. **Define male/1 and female/1**  
   - Specifies gender for individuals.

3. **Create rules father/2 and mother/2**  
   - Derive parental roles from parent facts.

4. **Define grandparent/2**  
   - Based on two parent relations.

5. **Create siblings/2**  
   - If they share a parent and are not the same person.

6. **Query relationships**  
   - Use defined facts and rules to infer family relations.

---

## Code
[`family-facts.pl`](family-facts.pl)

---

## Output
![Family Facts Output](output-images/3-b-family-facts-output.png)

---

## Result
The **family knowledge base** was successfully implemented in Prolog. Queries correctly inferred relationships such as **father, mother, grandparent, and siblings** using logical rules.
