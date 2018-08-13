package no.uio.ifi.pascal2100.scanner;

import no.uio.ifi.pascal2100.main.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import java.io.*;

public class Scanner {
    public Token curToken = null, nextToken = null;

    private LineNumberReader sourceFile = null;
    private final String sourceFileName;

	private String sourceLine = "";
    private int sourcePos = 0;

    public Scanner(String fileName) {
        sourceFileName = fileName;
        try {
            sourceFile = new LineNumberReader(new FileReader(fileName));
        } catch (FileNotFoundException e) {
            Main.error("Cannot read " + fileName + "!");
        }
        readNextToken();
        readNextToken();

    }


    public String identify() {
        return "Scanner reading " + sourceFileName;
    }


    public int curLineNum() {
        return curToken.lineNum;
    }


    private void error(String message) {
        Main.error("Scanner error on line " + curLineNum() + ": " + message);
    }


    public void readNextToken() {
        curToken = nextToken;

        if (sourcePos >= sourceLine.length()) {
            readNextLine();
        }

        if (sourceLine == "") {
            nextToken = new Token(eofToken, getFileLineNum());
            Main.log.noteToken(nextToken);
            return;
        }
        char curC = sourceLine.charAt(sourcePos);
     /*   String token = "";*/

        /*System.out.println(curC);*/
        
        if (curC == ' '){
        		sourcePos++;
        		readNextToken();
               	}

       else if (curC == '\t'){
            	sourcePos++;
            	readNextToken();
                }
      else if (curC == '\'')
       {
           StringBuilder accum = new StringBuilder();
           String tok ="";
           // skip the '"'
           sourcePos++;

          if (sourceLine.charAt(sourcePos) == -1)
               System.out.println("Unterminated String literal");
           
           while(sourceLine.charAt(sourcePos)  != '\'')
           {
            
           		curC=sourceLine.charAt(sourcePos);
           		accum.append(curC);
           		sourcePos++;
           		
          }
         // skip the terminating "
            sourcePos++;
           tok += accum;
           nextToken = new Token("",tok , getFileLineNum());
           Main.log.noteToken(nextToken);
       }

       else if (curC == '<'){
            if (sourceLine.charAt(sourcePos+1) == '=') {
                nextToken = new Token(lessEqualToken, getFileLineNum());
                sourcePos++;
                    }
            
       	
       else if(sourceLine.charAt(sourcePos+1) == '>'){
                nextToken = new Token(notEqualToken, getFileLineNum());
                sourcePos++;
                    }
       		else{
       			nextToken = new Token(lessToken, getFileLineNum());
               }
                sourcePos++;
                Main.log.noteToken(nextToken);
       		}
    	else if (curC == '-'){
                nextToken = new Token(subtractToken, getFileLineNum());
                Main.log.noteToken(nextToken);
                sourcePos++;
            }
       else if (curC == '+'){
                nextToken = new Token(addToken, getFileLineNum());
                sourcePos++;
                Main.log.noteToken(nextToken);
            }
       else if (curC == ','){
                nextToken = new Token(commaToken, getFileLineNum());
                sourcePos++;
                Main.log.noteToken(nextToken);
            }
       else if (curC == '.'){
            if (sourceLine.charAt(sourcePos+1) == '.') {
                nextToken = new Token(rangeToken, getFileLineNum());
                sourcePos++;
                }
            else{
                nextToken = new Token(dotToken, getFileLineNum());
               }
                sourcePos++;
                Main.log.noteToken(nextToken);
       		}

       else if (curC == ':'){
             if (sourceLine.charAt(sourcePos+1) == '=') {
                 nextToken = new Token(assignToken, getFileLineNum());
                 sourcePos++;
                }
             else{
                  nextToken = new Token(colonToken, getFileLineNum());
                }
                sourcePos++;
                Main.log.noteToken(nextToken);
       		}
       else if (curC == '>'){
                if (sourceLine.charAt(sourcePos+1) == '=') {
                    nextToken = new Token(greaterEqualToken, getFileLineNum());
                    sourcePos++;
                }else{
                    nextToken = new Token(greaterToken, getFileLineNum());
                }
                sourcePos++;
                Main.log.noteToken(nextToken);
            	}
       else if (curC == '['){
                nextToken = new Token(leftBracketToken, getFileLineNum());
                sourcePos++;
                Main.log.noteToken(nextToken);
            }
       else if (curC ==  ']'){
                nextToken = new Token(rightBracketToken, getFileLineNum());
                sourcePos++;
                Main.log.noteToken(nextToken);
            }
       else if (curC == ';'){
                nextToken = new Token(semicolonToken, getFileLineNum());
                Main.log.noteToken(nextToken);
                sourcePos++;
            }
        else if (curC ==  '('){
                nextToken = new Token(leftParToken, getFileLineNum());
                sourcePos++;
                Main.log.noteToken(nextToken);
            }

        
        else if(curC ==  '/') { if(sourceLine.charAt(sourcePos+1) == '*') {     // comment handling
        	sourcePos += 2;
            while(true){
                if (sourceLine.charAt(sourcePos) == '*' && sourceLine.charAt(sourcePos+1) == '/') {
                    break;
                }
                sourcePos++;
                if (sourcePos >= sourceLine.length()) {
                    readNextLine();
                }
            }
        }
            sourcePos += 2;
            readNextToken();
        
     }
        
        
       else if (curC == '{'){               // comment handling
                while(curC != '}') {
                    sourcePos++;
                    if(sourcePos >= sourceLine.length()){
                        readNextLine();
                    }
                    curC = sourceLine.charAt(sourcePos);
                }
                sourcePos++;
                readNextToken();
            }
        else if (curC ==  ')'){
                    nextToken = new Token(rightParToken, getFileLineNum());
                    Main.log.noteToken(nextToken);
                    sourcePos++;
                    }
      /*  else if (curC == '\''){
                    nextToken = new Token("", sourceLine.substring(sourcePos+1, sourcePos+2), getFileLineNum());
                    Main.log.noteToken(nextToken);
                    sourcePos+=3;
                    }*/

       else if (curC == '='){
                nextToken = new Token(equalToken, getFileLineNum());
                Main.log.noteToken(nextToken);
                sourcePos++;
                }

       else if (curC == '*'){
                nextToken = new Token(multiplyToken, getFileLineNum());
                Main.log.noteToken(nextToken);
                sourcePos++;
                }
        else{
              if(isDigit(curC)){                     	//For digit token
        			String digit="";
        			while(isDigit(curC)){
					digit+=curC;
					sourcePos++;
					curC = sourceLine.charAt(sourcePos);
        			}
        			try{
					nextToken = new Token(Integer.parseInt(digit), getFileLineNum());
        				}catch(NumberFormatException e){
					error("Number is too big");
				}
			}

		//For letter token
        	else if(isLetterAZ(curC)){
				String s="";
				while(isLetterAZ(curC)||isDigit(curC)){
					s+=curC;
					sourcePos++;
                    curC = sourceLine.charAt(sourcePos);
				}
				nextToken = new Token(s, getFileLineNum());
        }
        		else{
        		Main.error ("Invalid token neither digit nor letter");
        		}
			 Main.log.noteToken(nextToken);

        	}
        }


    private void readNextLine() {
        if (sourceFile != null) {
            try {
                sourceLine = sourceFile.readLine();
                if (sourceLine == null) {
                    sourceFile.close();  sourceFile = null;
                    sourceLine = "";
                } else {
                    sourceLine += " ";
                }
                sourcePos = 0;
            } catch (IOException e) {
                Main.error("Scanner error: unspecified I/O error!");
            }
        }
        if (sourceFile != null)
            Main.log.noteSourceLine(getFileLineNum(), sourceLine);
    }


    private int getFileLineNum() {
        return (sourceFile!=null ? sourceFile.getLineNumber() : 0);
    }


    // Character test utilities:

    private boolean isLetterAZ(char c) {
        return 'A'<=c && c<='Z' || 'a'<=c && c<='z';
    }


    private boolean isDigit(char c) {
        return '0'<=c && c<='9';
    }


    // Parser tests:

    public void test(TokenKind t) {
        if (curToken.kind != t)
            testError(t.toString());
    }

    public void testError(String message) {
        Main.error(curLineNum(),
                "Expected a " + message +
                " but found a " + curToken.kind + "!");
    }

    public void skip(TokenKind t) {
        test(t);
        readNextToken();
    }
}