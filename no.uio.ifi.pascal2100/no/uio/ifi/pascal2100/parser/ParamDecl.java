package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.leftParToken;
import static no.uio.ifi.pascal2100.scanner.TokenKind.rightParToken;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;

public class ParamDecl extends PascalDecl {
	/**
	 * <h1>ParamDecl </h1>
	 *
	 * <p>Parse a Pascal ParamDecl  as per project jernbarndiagram</p>
	 *
	 * <p>Copyright (c) 2015 by Sameer Sawant</p>
	 * name--- :--- type-- name--
	 */
	public ParamDeclList pardeclList;
	 String name;
	TypeName tn;
	public ParamDecl nextpd;

	public ParamDecl(String id, int lNum) {
		super(id, lNum);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<param decl > " +name + " on line " + lineNum;
	}
	
	
	public static ParamDecl parse(Scanner s) {
		enterParser("param decl");
		s.test(nameToken);
		
		
		ParamDecl pd = new ParamDecl(s.curToken.id, s.curLineNum());
		pd.name =  s.curToken.id;
		System.out.println("find letter "+ s.curToken.id);
		s.readNextToken();
		s.skip(colonToken);
		pd.tn=TypeName.parse(s);pd.tn.pardecl=pd;
		
		leaveParser("param decl ");
	
		return pd;
		}


	@Override void prettyPrint() {
		Main.log.prettyPrint(name);
		/*System.out.println("here is param "+named);*/
		Main.log.prettyPrint(":");
		tn.prettyPrint();
		Main.log.prettyIndent();
	}

	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		
		
		if (tn != null) tn.check(curScope, lib);
		
	}

}
