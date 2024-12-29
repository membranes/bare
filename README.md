<br>

We can interact with the token classification project's model via an instance, i.e., container, of this repository's image.  It is initially set-up to use a machine's CPU (Central Processing Unit) device. **A later image update** will accept a `device` argument; its value will be either 'cpu' or 'cuda'.

<br>

### Reminder: Tags, Annotations, Categories

This table below summarises the categories of the tags, whereby

> tag = annotation &#x29FA; - &#x29FA; category.  

The annotation **"B"** denotes _beginning_, whereas **"I"** denotes _inside_.

| category | definition          | tags         |
|:---------|:--------------------|:-------------|
| org      | organisation        | B-ORG, I-ORG |
| per      | person              | B-PER, I-PER |
| tim      | time                | B-TIM, I-TIM |
| geo      | geographical entity | B-GEO, I-GEO |
| gpe      | geopolitical entity | B-GPE, I-GPE |
| O        | miscellaneous       |              |


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
