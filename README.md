# Problem Solving
> I like tackling problems when there are freedom to design, explore my creativity, and constnatly evolving rather than accepting the current solution.
| HTMLSyntaxChecker   | java  |
| ImplementDatabase   | python, system design      |

# Approach
> I listed a brief explanation on how I approached each problem. 

1. Each problem was given one or two sentence of details of the problem.
2. What's next? Well, clearly, senders of the problems are my "customers". ask them to clarify any ambiguity. This also includes definiting assumptions and verifying a couple of use cases.
3. Given that we have use cases and clarifications, now what are my requirements for this system design?
4. Draw out brief class, methods, inheritance and association structures. Also, writing test cases in advance.
5. Wait to implement it, start writing skeleton of each class, methods and variables (no implementations) based on the structure designs I determined on step 4.
6. Start filling out missing implementations. 
7. Start debugging the problem! I have test cases defined early on. Let's use that to see what happens.
8. Of course if your test cases pass for one time run, you are a genius or your test case sucks. I had to debug and fix multiple times.
9. Once pre-defined test cases are passed, think of more test cases to work around the edge cases.

# Styling
#### Design
Clearly, I gather as much information as I can before starting to style a program. Depending on the requirements and assumptions, I had to design a system carefully. For instance, the 'database' design problem was an interesting problem to work and brush up the class and inheritance structure.

#### Comments
I documented every single class, method and variable to indicate clearly what they mean and represent. I also asked my friends who have not seen the problems before to review the comments and if they make sense.

###### examples
```java
	/*
	 	Sanitized_Input function removes all texts between tags in a string,
	 	and stores only the HTML tags into an array. 
	 	@ param: string is each line extracted from the input file.
	 	@ return: an array of tags found from the line.
	 */
	private List<String> Sanitized_Input(String str){
		List<String> tags = new ArrayList<String>();
		try {
			StringBuffer sb = new StringBuffer();
			Pattern p = Pattern.compile(HTML_PATTERN);
			Matcher m = p.matcher(str);	
			while (m.find()) {
				tags.add(m.group());
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return tags;
	}
```
```python
	def setVal(self, name, value):
		"""Set the variable name to the value value. 
		   Neither variable names nor values will contain spaces.
		   @param: name corresponds to the variable name which later a value is assigned to.
		   @param: value corresponds to value that will be assigned to the name."""
		d = self.d
		d[name] = value
```

