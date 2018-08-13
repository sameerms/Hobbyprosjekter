package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import java.util.ArrayList;
import java.util.List;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;


/**
 * <h1>IfStatm</h1>
 *
 * <p>Parse a Pascal IfStatm as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class IfStatm extends Statement {
Expression exp;
Statement st,st2;


public static List <Statement>stmtlist = new ArrayList<Statement>(); 
	public IfStatm(int lNum) {
		super(lNum);
		// TODO Auto-generated constructor stub
	}
	
	

    /**
     * Parse a IfStatm.
     * @param Scanner Tokens.
     * @return the IfStatm object of the parse tree.
     *if ----expression---- then---- statement----- else----- statement
     */
	public static IfStatm parse(Scanner s) {
		// TODO Auto-generated method stub
		enterParser("if-statm");
		s.skip(ifToken);
		IfStatm ifs= new IfStatm(s.curLineNum());
		ifs.exp=Expression.parse(s);ifs.exp.ifstat=ifs;
		
		
		s.skip(thenToken);
		ifs.st=Statement.parse(s);ifs.st.ifsta=ifs;
		stmtlist.add(ifs.st);
		
		if(s.curToken.kind ==elseToken){
			
			s.skip(elseToken);
			ifs.st2=Statement.parse(s);/*ifs.st.ifsta=ifs;*/
			stmtlist.add(ifs.st2);
			/*s.readNextToken();*/
		
		}
		
		leaveParser("if-statm");
		
		return ifs;
	}
	
		@Override public String identify() {
			return "<if-statm> " + " on line " + lineNum;
			
	}

	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		Main.log.prettyIndent();
		Main.log.prettyPrint(" if ");
		exp.prettyPrint();
		Main.log.prettyPrint(" then ");
	
		Main.log.prettyIndent();
		st.prettyPrint();
		if (st2 !=null){
			Main.log.prettyOutdent();
			Main.log.prettyPrintLn();
			Main.log.prettyPrint("else ");
			Main.log.prettyIndent();
			st2.prettyPrint();
			Main.log.prettyOutdent();
			Main.log.prettyOutdent();
			Main.log.prettyOutdent();
		}
		
		}



	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		if (exp != null) exp.check(curScope, lib);
		if (st2 != null) st2.check(curScope, lib);
		
		
	}
	
}