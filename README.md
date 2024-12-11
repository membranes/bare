<br>

> [!IMPORTANT]
> These notes are in progress.

<br>

We can interact with the token classification project's model via an instance, i.e., container, of this repository's image.  Initially set-up to use a machine's CPU (Central Processing Unit) device. **A later image update** will accept an argument; either 'cpu' or 'cuda'.

<br>

### Reminder: Tags, Annotations, Categories

The table summarises the categories of the tags; tag = annotation &#x29FA; - &#x29FA; category.  The annotation **"B"** denotes _beginning_, whereas **"I"** denotes _inside_.

| category | definition          | tags         |
|:---------|:--------------------|:-------------|
| org      | organisation        | B-ORG, I-ORG |
| per      | person              | B-PER, I-PER |
| tim      | time                | B-TIM, I-TIM |
| geo      | geographical entity | B-GEO, I-GEO |
| gpe      | geopolitical entity | B-GPE, I-GPE |
| O        | miscellaneous       |              |


<br>

### Text Examples

There are numerous sentence/paragraph sources, examples:

* [Why the genetic-testing revolution left some people behind — and what to do about it](https://www.nature.com/articles/d41586-024-04046-1)
* [Brazilian president Lula alert, ’progressed well’ since intracranial surgery](https://www.theguardian.com/world/2024/dec/11/brazilian-president-lula-recovering-intracranial-surgery)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
