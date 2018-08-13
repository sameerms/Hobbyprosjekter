package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.nameToken;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;
import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;


/**
 * <h1>TypeDecl</h1>
 *
 * <p>Parse a Pascal TypeDecl as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class TypeDecl extends PascalDecl {

	/*type name ---= ----type ---;--*/
	public TypeDeclPart typdeclp;
	TypeName tn;
	Type t;
	String name;
	EnumLiteral tenum;
	EnumLiteral fenum;
	public TypeDecl nexttypedec;
	public TypeDecl(String id, int lNum) {
		super(id, lNum);
		// TODO Auto-generated constructor stub
	}

	
	@Override public String identify() {
		return "<Type decl> " + " on line " + lineNum;
	}
		
	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		if (tn!=null) tn.prettyPrint();
		Main.log.prettyPrint("=");
		if(t != null) t.prettyPrint();
		Main.log.prettyPrint(";");
		
		
	}

	
	
    /**
     * Parse a block.
     * @param Scanner Tokens.
     * @return the Block object of the parse tree.
     */
	
	public static TypeDecl parse(Scanner s) {
		// TODO Auto-generated method stub
		enterParser("type Decl");
		
		TypeDecl td= new TypeDecl (s.curToken.id,s.curLineNum());
		
		td.name=s.nextToken.id;
		td.tn=TypeName.parse(s);td.tn.tdecl=td;
		
		s.skip(equalToken);
		td.t= Type.parse(s);td.t.tdecl=td;
		
		s.skip(semicolonToken);
	
		
		
		leaveParser("type Decl");
		return td;
	}

	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		if (tn!=null) tn.check(curScope, lib);
		if(t!= null) t.check(curScope, lib);
	}

}
