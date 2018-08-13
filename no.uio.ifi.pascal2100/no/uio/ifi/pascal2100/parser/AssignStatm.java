package no.uio.ifi.pascal2100.parser;

import no.uio.ifi.pascal2100.main.*;
import no.uio.ifi.pascal2100.scanner.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import java.util.ArrayList;


/*variable ---:= ---expression*/

public class AssignStatm extends Statement {
	Variable vb;
	Expression exp;
	ArrayList<EnumLiteral> values = new ArrayList<EnumLiteral>();
	
	public AssignStatm(int lNum) {
		super(lNum);
		// TODO Auto-generated constructor stub
	}
	
	
	public static AssignStatm parse(Scanner s){
		enterParser("assign statm");
		
		AssignStatm as=new AssignStatm(s.curLineNum());
		as.vb=Variable.parse(s);

		
		s.skip(assignToken);
		as.exp=Expression.parse(s);
		
		
		leaveParser("assign statm");
		return as;
	}
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<assign statm> "  + " on line " + lineNum;
	}

	@Override void prettyPrint() {
		Main.log.prettyPrintLn();
		Main.log.prettyIndent();
		if (vb!=null)vb.prettyPrint();
		Main.log.prettyPrint(":=");
		if (exp!=null)exp.prettyPrint();
		
		
		}


	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		if (vb!=null)vb.check(curScope,lib);
		if (exp!=null)exp.check(curScope,lib);
	}
		

}