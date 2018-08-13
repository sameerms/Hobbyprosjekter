package no.uio.ifi.pascal2100.parser;

import no.uio.ifi.pascal2100.main.*;
import no.uio.ifi.pascal2100.scanner.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;
		/* <program> ::= � program � <name> �;� <block> �.� */
public class Program extends PascalDecl {
	Block progBlock;
	Program(String id, int lNum) {
		
		super(id, lNum);
		}
	@Override public String identify() {
		return "<program> " + name + " on line " + lineNum;
		}

	public static Program parse(Scanner s) {
		enterParser("program");
		
		s.skip(programToken);
		s.test(nameToken);
		Program p = new Program(s.curToken.id, s.curLineNum());
		s.readNextToken();
		s.skip(semicolonToken);
		
		p.progBlock = Block.parse(s); p.progBlock.context = p;
		s.skip(dotToken);
		
		leaveParser("program");
		
		return p;
		}


	 @Override
	public void prettyPrint() {
		 	Main.log.prettyPrintLn();
			Main.log.prettyPrint("program ");
			Main.log.prettyIndent();
			Main.log.prettyPrint(name);
			Main.log.prettyPrintLn(" ; ");
			progBlock.prettyPrint();
			Main.log.prettyPrint(".");
			
			
		 
		 
	}
	
		
	
	public void genCode(CodeFile code) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		System.out.println("program"+curScope);
		
		/*curScope.addDecl(name,this);
		PascalDecl d = curScope.findDecl(name,this);*/
		
		if(progBlock != null) progBlock.check(curScope,lib);
		
		
	}
}