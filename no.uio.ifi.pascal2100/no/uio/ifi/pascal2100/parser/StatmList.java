package no.uio.ifi.pascal2100.parser;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import java.util.ArrayList;
import java.util.EnumSet;
import java.util.List;

public class StatmList extends PascalSyntax {

	public Block b;
	Statement stmt;
	public Statement firststmt;
	public CompoundStatm compnd;
	public ArrayList <Statement>stmtlist = new ArrayList<Statement>(); 

	public StatmList(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}
	
	
	/**
     * Parse a StatmList.
     * @param Scanner Tokens.
     * @return the StatmList object of the parse tree.
     */

	public static StatmList parse(Scanner s) {
		
		enterParser("statm list");
		/*System.out.println("entering persor statm list");*/
		StatmList st = new StatmList(s.curLineNum());
		
		st.firststmt=Statement.parse(s);
		st.stmtlist.add(st.firststmt);
		Statement tempStmt=st.firststmt;
		
		while (s.curToken.kind == semicolonToken){
			s.skip(semicolonToken);
			tempStmt.nextstmt= tempStmt=Statement.parse(s);
			st.stmtlist.add(tempStmt);
	}
		
	
		leaveParser("statm list");
		return st;
	}
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<statm list> "  + " on line " + lineNum;
	}

	@Override void prettyPrint() {
	
		Statement localst= firststmt;
		while (localst!=null){
			localst.prettyPrint();
		
		localst=localst.nextstmt;
		if(localst != null)Main.log.prettyPrint(" ; ");
		Main.log.prettyPrintLn();
		}
		
		
		
		
		}


	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		Statement localst= firststmt;
		while (localst!=null){
			localst.check(curScope, lib);
		
		localst=localst.nextstmt;
		
		}
		
	}
		
}
