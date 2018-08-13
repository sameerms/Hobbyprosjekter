package no.uio.ifi.pascal2100.parser;

import  no.uio.ifi.pascal2100.scanner.*;
import no.uio.ifi.pascal2100.main.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

public class EnumType extends Type {
EnumLiteral firstel,el2 ;
public String name;
	public EnumType(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}
	

    /**
     * Parse a EnumType.
     * @param Scanner Tokens.
     * @return the EnumType object of the parse tree.
     * Used linked list for objects
     */
	public static EnumType parse(Scanner s) {
		enterParser("enum-type");
		
		s.skip(leftParToken);
		
		EnumType et= new EnumType(s.curLineNum());
		et.firstel = EnumLiteral.parse(s);
		EnumLiteral tempEl=et.firstel;
		
		
			while (s.curToken.kind == commaToken){
				s.skip(commaToken);
				tempEl.nextEt= tempEl=EnumLiteral.parse(s);
				
		}
		
		s.skip(rightParToken);
		
		leaveParser("enum-type");
		return et;
}
	
	@Override public String identify() {
		return "<enum-type> " +  " on line " + lineNum;
		}
	
	
	
	 @Override
		public void prettyPrint() {
			// TODO Auto-generated method stub
			
		 Main.log.prettyPrint("( "); 
			
		 EnumLiteral localel= firstel;
			while (localel!=null){
				localel.prettyPrint();
			
				localel=localel.nextEt;
			if(localel!= null)Main.log.prettyPrint(" , ");
			
			}
			 Main.log.prettyPrint(" )");
			 Main.log.prettyIndent();
			}


	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		 EnumLiteral localel= firstel;
			while (localel!=null){
				localel.check(curScope,lib);
			
				localel=localel.nextEt;
			
			
			}
		
		
	} 
		
		
		}

