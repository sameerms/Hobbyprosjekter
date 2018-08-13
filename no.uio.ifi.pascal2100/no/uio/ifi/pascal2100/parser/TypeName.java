package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.nameToken;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;

public class TypeName extends Type {

	public TypeDecl tdecl;
	public FuncDecl tpname;
	public ParamDecl pardecl;
	 String name;

	public TypeName(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}

	@Override public String identify() {
		return "<type name> " + " on line " + lineNum;
		}

	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		Main.log.prettyPrint(name );
	}

	public static TypeName parse(Scanner s) {
		// TODO Auto-generated method stub
		enterParser("type name");
		s.test(nameToken);
		
		TypeName tpn= new TypeName(s.curLineNum());
		tpn.name=s.curToken.id;
		
		tpn.tnam.add(tpn);
		s.readNextToken();
		leaveParser("type name");
		return tpn;
	}

	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		System.out.println("here typename"+name+ "  "+lineNum);
		PascalDecl d2 = curScope.findDecl(name,this);
		 
		
		
		
	


	}
}
