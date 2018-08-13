package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;

public class EmptyStatm extends Statement {

	public EmptyStatm(int lNum) {
		super(lNum);
		// TODO Auto-generated constructor stub
	}


	public static EmptyStatm parse(Scanner s) {
		
		enterParser("empty statm");
		EmptyStatm es= new EmptyStatm(s.curLineNum());
		
		leaveParser("empty statm");
		return es;
	}
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<empty statm> "  + " on line " + lineNum;
	}

	@Override void prettyPrint() {
	
		Main.log.prettyPrint("");
		}


	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		
	}
		
}