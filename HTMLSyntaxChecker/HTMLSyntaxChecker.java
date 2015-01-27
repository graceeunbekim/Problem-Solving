/*
 * Author: Grace Eunbe Kim
 * Contact: eunbegracekim40@gmail.com
 * Salesforce RPT 
 * HTML Syntax Checker
 */
import java.io.*; 
import java.util.*;
import java.io.File;
import java.util.HashMap; 
import java.lang.Exception;
import java.util.Collections; 
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class HTMLSyntaxChecker{

	/*
	 Max length of input lines must be less than 32727.
	 constant variables to determine the success and error messages for
	 HTML Syntax Checker. 
	 */
	private static final Integer MAX_LENGTH = 32727;
	private static final String INCORRECT_FILE = "file is incorrectly formatted. Check the length.";
	private static final String SUCCESS = "OK";
	private static final String BAD_CHARATER = "bad character in tag name.";
	private static final String BAD_LENGTH = "too many/few characters in tag name.";
	private static final String NO_CLOSING_TAG = "expected %s.";
	private static final String NO_BEGIN_TAG = "no matching begin tag.";

	/*
	 Constant variables that are used for pattern matching for regular expressions.
	 */
	private static final String HTML_PATTERN = "(?i)(<[a-zA-Z]+>)|(?i)(</[a-zA-Z]+>|<>|<[a-zA-Z]+)";
	private static final String NULL_TAG = "<>";
	private static final String CLOSING_TAG_INDICATOR = "</";
	private static final String OPENING_TAG_INDICATOR = "<";
	private static final String INCORRECT_FORMAT = "<[a-zA-Z]+";

	/*
	 Parse HTML reads a txt file line by line and store it in a hashmap. The
	 output hashmap will be used to determine the error or success messages.
	 @ param: a text input_html, including number of lines in the text, and html text.
	 @ return: a hash map of key as the line number and values as an array of tags.
	 */
	private HashMap<Integer, List<String>> Parse_HTML(String filename){
		HashMap<Integer, List<String>> map = new HashMap<Integer, List<String>>();

		try{
			BufferedReader in = new BufferedReader(new FileReader(filename));
			StringBuffer sb = new StringBuffer();
			String line;

			while ((line = in.readLine()) != null) {
				sb.append(line);
				sb.append('\n');
            }
        	in.close();

        	String[] splitted = sb.toString().split("\n");
        	int line_number = 1;
        	for (int i=0; i < splitted.length; i++){
        		map.put(line_number, Sanitized_Input(splitted[i]));
        		line_number++;
        		
        	}

        	System.out.println(map.toString());

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return map;
	}	

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

	/*
		Determine Error() takes a map with a key corresponds to a line number and the value
		equals to string text of the line. 
	 */
	private String Determine_Error(HashMap<Integer, List<String>> map){
		List<String> begin_tags = new ArrayList<String>();
    	List<String> close_tags = new ArrayList<String>();
		
    	if (map.size() <= 1){
    		return INCORRECT_FILE;
    	}

		for (Integer key : map.keySet()) {
    		List<String> value = map.get(key);
    		for (String tag : value) {

    			// case: null tag, incorrect length
    			if (tag.matches(NULL_TAG)) {
    				return String.format("line %d: " + BAD_LENGTH, key);
    			}

    			// case: incorrect format
    			if (tag.matches(INCORRECT_FORMAT)) {
    				return String.format("line %d: " + BAD_CHARATER, key);
    			}

    			if (tag.contains(CLOSING_TAG_INDICATOR)){
    				close_tags.add(tag.replace("/",""));
    			}
    			else if (tag.contains(OPENING_TAG_INDICATOR)) {
    				begin_tags.add(tag);
    			}
    		}

    		
		}
		System.out.println(close_tags);
    	System.out.println(begin_tags);


    	// missing tags when two close and open arrays are different size.
    	if (close_tags.size() != begin_tags.size()){
			// case: no matching begin tag.
    		if (close_tags.size() > begin_tags.size()) {
    			close_tags.removeAll(begin_tags);
    			String val = close_tags.get(0).replace(OPENING_TAG_INDICATOR, 
    													CLOSING_TAG_INDICATOR);
    			Integer res = Get_Key_BY_Value(map, val);
    			return String.format("line %d: " + NO_BEGIN_TAG, res);
    		}

    		// case: no matching close tag.
    		else {
    			begin_tags.removeAll(close_tags);
    			String val = begin_tags.get(0);
    			Integer res = Get_Key_BY_Value(map, val);
    			return String.format("line %d: " + NO_CLOSING_TAG, 
    											res, 
    											val.replace(OPENING_TAG_INDICATOR, CLOSING_TAG_INDICATOR));
    		}

    	// missing tags when two close and open arrays are the same size.
    	} else {
    		if (!close_tags.equals(begin_tags)) {
    			String val = begin_tags.get(0);
    			Integer res = Get_Key_BY_Value(map, val);
    			return String.format("line %d: " + NO_CLOSING_TAG, 
    											res, 
    											val.replace(OPENING_TAG_INDICATOR, CLOSING_TAG_INDICATOR));
    		}
    	}
		return SUCCESS;
	}

	/*
		Get_Key_By_Integer finds a key by value in a hashmap. This function is used to retrieve
		a line number where an error is found to display on command line.
		@ param: hash map of keys and values
		@ value: a string value to find the key for the line number where an error occurs.
	 */
    private Integer Get_Key_BY_Value(HashMap<Integer, List<String>> map, String value) {
    	Integer key = 0;
        for (Map.Entry<Integer, List<String>> entry : map.entrySet()) {
        	List<String> values = entry.getValue();
            for (String val : values) {
            	if (val.equals(value)) {
                	key = entry.getKey();
            	}
            }
        }
        return key;
    }

	/*
		Main function needs to take a name of text file with HTML string.
		@ param: text file which needs to be eximined for a propor tag usage.
		i.e. javac HTMLSyntaxChecker.java
			 java HTMLSyntaxCheck test_cases/test_case1.java
	 */
	public static void main(String args[]) {
		HTMLSyntaxChecker htmlsyntaxchecker = new HTMLSyntaxChecker();
		HashMap<Integer, List<String>> output = htmlsyntaxchecker.Parse_HTML(args[0]);
		String res = htmlsyntaxchecker.Determine_Error(output);
		System.out.println(res);
	}

}