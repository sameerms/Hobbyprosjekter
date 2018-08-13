package no.uio.ifi.pascal2100.parser;

import no.uio.ifi.pascal2100.scanner.Scanner;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;


public class InnerExp extends Factor {

	public Factor fa;
	public Expression exp;

	public InnerExp(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}
	public static InnerExp parse(Scanner s) {
		enterParser("inner exp");
		InnerExp inexp = new InnerExp(s.curLineNum());
		s.skip(leftParToken);
		inexp.exp=Expression.parse(s);inexp.exp.inex= inexp;
		s.skip(rightParToken);
		leaveParser("inner exp ");
		return inexp;
	}
	
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<inner exp> " + " on line " + lineNum;
	}
	@Override void prettyPrint() {


		
		Main.log.prettyPrint("(");
		exp.prettyPrint();
		
		Main.log.prettyPrint(")");
		
		}
	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		if (exp != null)exp.check(curScope, lib);
	}
	
}
